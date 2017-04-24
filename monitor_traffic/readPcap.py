# rang1

# 1) main() get arguments
# 2) getPorts() get all the ports that were used to retrieve our flag from the service
# 3) getConversations() from the list of ports, compare the src and dst to filter all the tcp conversations and write to file
# 4) getRaw(). from the total number of flags sent out, read the filtered pcap using tshark
#       the total number of flags sent are equal to conversations
#       tshark will then extract the conversation
# 4.1) python will then extract tshark's output
# 4.2) send src_port, dst_port, timestamp, raw, and raw length to database
import psycopg2 as psycopg2
from scapy.all import *
from datetime import datetime

import argparse, re

DEBUG = 0
countFlag = 0
flagsArr = ['FLG', 'Note content']  # If we find a string with more flags, add them here
portArr = []  # Store all the ports here. Not sure
serviceArr = [20001, 20002, 20003]  # store all service ports here. to be compared when sending to database
tSharkDelimiter1 = "Follow: "
dateTimeFormat = '%Y-%m-%d %H:%M:%S.%f'


# this is will run a loop from 0 to countFlag inclusive.
#  cmd is 'tshark -r pcap -z follow,tcp,ascii,[num]
# take the output of this and only get the text between all the equals and put into an output
def getRaw(file):
    global countFlag, tSharkDelimiter1
    outFile = "%s.rawConver" % file
    cmd = "touch %s" % outFile
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)  # make sure to create the file first

    regex = re.compile(r":([\d]+)")
    postgres = dbClientHandler()

    for i in xrange(0, countFlag + 1):
        cmd = "tshark -r %s.filtered -z follow,tcp,ascii,%d" % (file, i)
        # print i # DEBUG
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        output = proc.stdout.read()
        # http://stackoverflow.com/a/3368991
        try:
            start = output.index(tSharkDelimiter1)
            raw = output[start:]

            # run regex on raw, get ports
            # --------------------
            resultPorts = regex.findall(raw)
            # if port 0 is IN serviceArr, mark that as dst for database
            # else, mark as src.
            port0 = int(resultPorts[0])
            if port0 in serviceArr:
                dst = port0
                src = int(resultPorts[1])
            else:
                dst = int(resultPorts[1])
                src = port0
            # --------------------

            # build time
            time = datetime.now().strftime(dateTimeFormat)

            # get raw payload
            # --------------------
            listNewLine = find(raw, '\n')
            payload = raw[listNewLine[4]:listNewLine[-2]]
            lengthPay = listNewLine[-2] - listNewLine[4]

            # prepare query
            query = "INSERT INTO payloads(src_port, dst_port, timestamp, payload,length) " \
                    "VALUES (%d,%d,'%s','%s',%d);" % (src, dst, time, payload, lengthPay)

            if dst != 0:
                # only insert query if the dst is NOT 0, which means off by one error
                postgres.execute(query)

            with open(outFile, 'a') as fd:
                fd.write(raw)

        except ValueError:
            return ""

    print "Look for %s file" % outFile


def getConversations(file):
    global portArr
    pcap = rdpcap(file)

    for pkt in pcap:
        if pkt[TCP].sport in portArr or pkt[TCP].dport in portArr:
            # use sport, because this conversation started from this port
            # use dport, because our server returned the flag
            wrpcap(file + ".filtered", pkt, append=True)

    print "Look for %s.filtered file" % file


def getPorts(source, file):
    global countFlag, portArr

    pcap = rdpcap(file)

    if DEBUG:
        total = 0
    for pkt in pcap:
        if DEBUG:
            total += 1
            print "[DEBUG] \n" + str(pkt.summary)

        if pkt[IP].src == source and Raw in pkt:
            # look for any flags leaving our source ip and make sure the packet has RAW layer
            if DEBUG:
                print "[DEBUG IP] \n" + str(pkt.summary)
            if any(flag in pkt[Raw].load for flag in flagsArr):
                if DEBUG:
                    print "[DEBUG RAW] \t" + str(pkt.summary)
                countFlag += 1
                portArr.append(pkt[TCP].dport)

    if DEBUG:
        print "%d total packets" % total


# http://stackoverflow.com/a/11122355
# Gets a list of occurrences of the character 'ch' in string 's'
def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def dbClientHandler():
    '''
    :return: db handler
    '''
    try:
        conn = psycopg2.connect(
            "dbname='dau3slm4jue1qn' user='viicslnyyexdxx' host='ec2-54-221-254-72.compute-1.amazonaws.com' password='301287f0b3bbdffd7fe9684487ebb483b11d0e608f7432500c2d508afa99e140'")
        conn.autocommit = True

        cur = conn.cursor()

        return cur
    except Exception as e:
        print 'Unable to connect to database...' + e.message


def main():
    global countFlag

    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source-ip', required=True)
    parser.add_argument('-p', '--pcap', required=True)
    args = vars(parser.parse_args())
    source = args['source_ip']
    file = args['pcap']

    getPorts(source, file)
    print "There were %d flags sent out" % countFlag
    print "Now getting the conversations"
    getConversations(file)
    print "Now extracting conversations"
    getRaw(file)


if __name__ == '__main__':
    main()

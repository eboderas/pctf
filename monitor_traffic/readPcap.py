

# rang1

# 1) main() get arguments
# 2) getPorts() get all the ports that were used to retrieve our flag from the service
# 3) getConversations() from the list of ports, compare the src and dst to filter all the tcp conversations and write to file
# 4) getRaw(). from the total number of flags sent out, read the filtered pcap using tshark
#       the total number of flags sent are equal to conversations
#       tshark will then extract the conversation
# 5) python will then extract just the last part, which is raw payload, and place into a file.
#     we can extend this by taking "raw" variable and inserting into a database

from scapy.all import *
import argparse, re

DEBUG = 0
countFlag = 0
flagsArr = ['FLG', 'Note content']  # If we find a string with more flags, add them here
portArr = []  # Store all the ports here. Not sure
serviceArr = [20001, 20002, 20003] #store all service ports here. to be compared when sending to database
tSharkDelimiter1 = "Follow: "


# this is will run a loop from 0 to countFlag inclusive.
#  cmd is 'tshark -r pcap -z follow,tcp,ascii,[num]
# take the output of this and only get the text between all the equals and put into an output
def getRaw(file):
    global countFlag, tSharkDelimiter1
    cmd = "touch %s.rawConver" % file
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)  # make sure to create the file first

    regex = re.compile(r":([\d]+)")


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
            resultPorts = regex.findall(raw)
            # if port 0 is IN serviceArr, mark that as dst for database
            # else, mark as src.
            with open("rawConversations", 'a') as fd:
                fd.write(raw)

        except ValueError:
            return ""


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
    #getConversations(file)
    print "Now extracting conversations"
    getRaw(file)


if __name__ == '__main__':
    main()

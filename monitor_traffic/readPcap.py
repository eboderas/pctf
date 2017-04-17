#!/usr/bin/env python

# rang1

# 1) main() get arguments
# 2) getPorts() get all the ports that were used to retrieve our flag from the service
# 3) getConversations() from the list of ports, compare the src and dst to filter all the tcp conversations and write to file

from scapy.all import *
import argparse

DEBUG = 0
countFlag = 0
flagsArr = ['FLG', 'Note content']  # If we find a string with more flags, add them here
portArr = []  # Store all the ports here. Not sure


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
        total=0
    for pkt in pcap:
        if DEBUG:
            total+=1
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
    getConversations(file)


if __name__ == '__main__':
    main()

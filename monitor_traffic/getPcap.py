#!/usr/bin/env python
# rang1

# This python records all packets for 5 minutes and stores into 'tick[num].pcap'

from scapy.all import *

tick = 0
file = "temp"  # should get overwritten by handle_packet()


def handle_packet(packet):
    global tick, file
    file = "tick%d.pcap" % tick
    wrpcap(file, packet, append=True)


def main():
    global tick, file
    filtr = "tcp"

    min = 5
    sec = min * 60
    while 1:
        sniff(prn=handle_packet, filter=filtr, store=0, timeout=sec)
        tick += 1
        print "wrote %s" % file


if __name__ == '__main__':
    main()

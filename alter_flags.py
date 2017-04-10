#########################
## Connor Nelson, 2017 ##
#########################

# Redirect outgoing game network packets to alter_flags network (172 --> 10):
# iptables -t nat -A OUTPUT -d 172.31.129.0/24 -j NETMAP --to 10.31.129.0/24

# Create virtual interface for alter_flags network
# modprobe dummy
# ip link set name alter_flags dev dummy0
# ip addr add 10.31.129.0/24 brd + dev alter_flags
# ifconfig alter_flags up

# Note: this can all be undone with:
# iptables -t nat -D OUTPUT -d 172.31.129.0/24 -j NETMAP --to 10.31.129.0/24
# ip addr del 10.31.129.0/24 brd + dev alter_flags
# ip link delete alter_flags type dummy
# rmmod dummy

# Note: packets sent with scapy seem to bypass iptables (or atleast OUTPUT)

import string
import re
import random

from scapy.all import sendrecv, IP

def alter_flags(packet):
    flag_chars = string.digits + string.ascii_uppercase + string.ascii_lowercase
    payload = str(packet[IP].payload)
    m = re.search('FLG[%s]{7}' % (flag_chars,), payload)
    if m:
        flag = m.group(0)
        fake_flag = 'FLG' + ''.join(random.choice(flag_chars) for _ in range(7))
        print flag, '-->', fake_flag
        packet[IP].payload = payload.replace(flag, fake_flag)
        
    del packet[IP].chksum
    packet[IP].dst = '172' + packet[IP].dst[2:]
    sendrecv.send(packet[IP])

def main():
    sendrecv.sniff(iface = 'alter_flags',
                   lfilter = lambda p: IP in p and '10.31.129' in p[IP].dst,
                   prn = alter_flags)

if __name__ == '__main__':
    main()

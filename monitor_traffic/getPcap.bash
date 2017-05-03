#!/bin/bash
#overview    rang1
# 1) check for root
# 2) get arguments.
#     the port number to ssh could be different. use args to change everytime
# 3) run tcpdump and export port.
# 4) write to temp[num].pcap file


if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   echo "Ubuntu users: type: \"sudo bash ${0##*/}\". It will ask for user's password"
   exit 1
fi

# http://stackoverflow.com/a/14203146
# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.
port=""
i="11"

function show_help {
echo "Usage: bash ${0##*/} [-h] -p <port>"
echo -e "\t where -h is to show this help window"
echo -e "\t where -p is the port NOT to include in tcpdump"
               exit 0
           }
while getopts "h?p:" opt; do
    case "$opt" in
    h|\?)
        show_help
        exit 0
        ;;
    p)  port=$OPTARG
        ;;
    esac
done
shift $((OPTIND-1))
[ "$1" = "--" ] && shift

if [[ -z  $port  ]]; then
#show help and exit if the user did not use "-p"
show_help
fi

# write to temp[num].pcap
#   write to numbered files just in case we forget to scp the pcap and overwrite the previous
while true; do
tcpdump port not $port and port not ssh and port not 443 -w temp$i.pcap &
pid=$!
sleep 300
kill $pid
echo "Killed tcpdump"
i=$[$i+1]
done

#!/bin/bash


# http://stackoverflow.com/a/14203146
# A POSIX variable
OPTIND=1         # Reset in case getopts has been used previously in the shell.
src_ip=""
i="0"

function show_help {
echo "Usage: bash ${0##*/} [-h] -s <src_ip>"
echo -e "\t where -h is to show this help window"
echo -e "\t where -s is the source ip for readPcap.py"
               exit 0
           }
while getopts "h?s:" opt; do
    case "$opt" in
    h|\?)
        show_help
        exit 0
        ;;
    s)  src_ip=$OPTARG
        ;;
    esac
done
shift $((OPTIND-1))
[ "$1" = "--" ] && shift


if [[ -z  $src_ip  ]]; then
	# show help and exit if the user did not use "-s"
	show_help
fi

mkdir finished

while true; do
	if [ $(git rev-parse HEAD) = $(git ls-remote $(git rev-parse --abbrev-ref @{u} | \sed 's/\// /g') | cut -f1) ]; then
		echo up to date
	else
		echo not up to date
		git pull
		python readPcap.py -s $src_ip -p temp$i.pcap
		i=$[$i+1]
		cp temp$i.pcap finished
	fi
done

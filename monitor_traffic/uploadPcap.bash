#!/bin/bash

# tcrosenk

# overview:
# this should be run concurrently with getPcap.bash
# pcap files get created instantly every 5 minutes
# so to test when a pcap file is ready to be pushed
# to github, it should exist and the next pcap should 
# exist as well. 


# set up github credentials to not be required for
# the next 3 hours.
git config credential.helper store
git config credential.helper cache
git config credential.helper 'cache --timeout=10800'

i="0"
j="1"

while true; do
	if test -e temp$i.pcap; then
		if test -e temp$j.pcap; then

			# push the current pcap file to the repo
			git add temp$i.pcap
			git commit -m "pushing temp$i.pcap"
			git push -u origin master

			# increment i and j to move onto next pcap file
			i=$[$i+1]
			j=$[$j+1]
			
		fi
	fi
done
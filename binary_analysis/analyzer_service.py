#!/usr/bin/env python
#Idea is inspired by Connor
import sys
import os

def overflow_exploit():
	return 0

def command_injection():
	return 0

def path_exploit():
	return 0

def binary_category():
	return 0

def containsVuln(addresses):
	vulnLine = os.popen('objdump -d a.out | grep -oP "\d.*(strcpy)"').read()
	vulnCalls = vulnLine.split("\n") 
	onlystrcpy = list(filter(lambda x:"\t" in x, vulnCalls))
	return onlystr

vuln_funs = filter(None,os.popen('objdump -d '+ sys.argv[1] +  ' | grep -oP "(strcpy|memcpy|scanf|printf)"').read().split('\n'))
print vuln_funs
vuln_set = set(vuln_funs)
print "This program has these vulnerable functions:\n" + str(vuln_set)

startAddresses = os.popen('objdump -d a.out | grep -P "^<*(?=.*(>:))"').read()
#print startAddresses

listAddresses = startAddresses.split("\n")
#print listAddresses 

goodAddresses = list(filter(lambda x: not "@" in x, listAddresses))
print goodAddresses

test = containsVuln(goodAddresses)
print test
print "Calls:\n" + str(test)

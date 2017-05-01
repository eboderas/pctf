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
	vulnLine = os.popen('objdump -d a.out | grep -oP "\d.*(strcpy|printf|scanf)"').read()
	vulnCalls = vulnLine.split("\n") 
	vulninstrList = list(filter(lambda x:"\t" in x, vulnCalls))
	vulnAddr = []
	for i in vulninstrList:
		addr = i[0:7]
		vulnAddr.append(int("0x" + addr, 16))
	functionAddr = []
	for i in addresses:
		addr = i[0:8]
		#print addr
		if addr != "":
			functionAddr.append(int("0x" + addr, 16))
	#print vulninstrList
	#print vulnAddr

	#print addresses
	#print functionAddr
	toPrint = []
	for i in range(0, len(vulnAddr)):
		minJ = -1
		for j in range(0, len(functionAddr)):
			function = 9999999
			if (vulnAddr[i] > functionAddr[j] and vulnAddr[i]-functionAddr[j] < function):
				function = vulnAddr[i]-functionAddr[j]
				minJ = j
		
		toPrint.append(str(vulninstrList[i] + "\n") + " belongs in\n" + str(addresses[minJ]))		
	return toPrint

vuln_funs = filter(None,os.popen('objdump -d '+ sys.argv[1] +  ' | grep -oP "(strcpy|memcpy|scanf|printf)"').read().split('\n'))
#print vuln_funs
vuln_set = set(vuln_funs)
print "This program has these vulnerable functions:\n" + str(vuln_set)

startAddresses = os.popen('objdump -d a.out | grep -P "^<*(?=.*(>:))"').read()
#print startAddresses

listAddresses = startAddresses.split("\n")
#print listAddresses 

goodAddresses = list(filter(lambda x: not "@" in x, listAddresses))
#print goodAddresses

test = containsVuln(goodAddresses)
for i in test:
	print i + "\n"

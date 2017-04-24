#!/usr/bin/python

"""
Author: Erik Trickel (erik@trickel.com)
Exploring angr with fauxware 
Created: June 3, 2016

"""

import angr
from utils import bcolors

def main():
	proj = angr.Project('./fauxware',  load_options={'auto_load_libs': False})

	cfg = proj.analyses.CFGAccurate(keep_state=True)

	print "It has %d nodes and %d edges" % (len(cfg.graph.nodes()), len(cfg.graph.edges()))
	
	entry_node = cfg.get_any_node(proj.entry)

	# we can also look up predecessors and successors
	print "Predecessors of the entry point:", entry_node.predecessors
	print "Successors of the entry point:", entry_node.successors

	cnt = 1
	col_width=0

	# get largest entry to print the output pretty in 2 columns
	for v in cfg.kb.functions :
		tempStr = "%s%s%s at 0x%x" % (bcolors.OKBLUE, cfg.kb.functions[v].name, bcolors.ENDC, v)
		col_width = max (col_width, len(tempStr))

	col_width = col_width + 1 # for padding between
	
	# loop through functions and print out with functions in BLUE
	strOut = ""
	for v in cfg.kb.functions :
		tempStr = "%s%s%s at 0x%x" % (bcolors.OKBLUE, cfg.kb.functions[v].name, bcolors.ENDC, v)
		strOut += tempStr.ljust(col_width)
		if (cnt % 2 == 0 and cnt > 0 or (col_width-len(bcolors.OKBLUE)-len(bcolors.ENDC)) >= 40) :
		 	strOut += "\n"
		cnt = cnt +1
	print strOut
 	
	# Get the object to explore the different path groups
	pg = proj.factory.path_group()

	# keep exploring the binary until "Congrats" appears in the stdout 
	pg.explore(find=lambda p: "Welcome" in p.state.posix.dumps(1))

	# grab the state of the path once the condition above is set
	s = pg.found[0].state

	# print the program stdout dump at the state
	print s.posix.dumps(1)

	# set flag = to the data sent into the program
	flag = s.posix.dumps(0)

	print("The Password is '" + bcolors.OKBLUE + flag + bcolors.ENDC + "'")


if __name__ == '__main__':
	main()



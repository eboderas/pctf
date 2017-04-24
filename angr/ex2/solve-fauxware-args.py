#!/usr/bin/python

"""
Author: Erik Trickel (erik@trickel.com)
Created: July 21, 2016

"""

import angr
OKBLUE = '\033[94m'
ENDC = '\033[0m'


def main():
	proj = angr.Project('./fauxware-args', load_options={"auto_load_libs": False})
	argv1 = angr.claripy.BVS("argv1", 0xE * 8)
	argv2 = angr.claripy.BVS("argv2", 0xE * 8)

	initial_state = proj.factory.entry_state(args=["./fauxware", argv1, argv2]) 

	
	# Get the object to explore the different path groups
	pg = proj.factory.path_group(initial_state)

	# keep exploring the binary until "Congrats" appears in the stdout 
	pg.explore(find=lambda p: "Welcome" in p.state.posix.dumps(1))

	# grab the state of the path once the condition above is set
	s = pg.found[0].state

	# print the program stdout dump at the state
	print s.posix.dumps(1)

	# set solution = to the value used in argv2
	solution = s.se.any_str(argv2)
	solution = solution.replace("\x00","");
	return solution

if __name__ == '__main__':
	print("The solution is '" + OKBLUE + repr(main()) + ENDC + "'")


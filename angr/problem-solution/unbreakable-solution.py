#!/usr/bin/python

"""
Author: Erik Trickel (erik@trickel.com)
Created: July 21, 2016

"""

import angr
OKBLUE = '\033[94m'
ENDC = '\033[0m'

def main():
	binName = './unbreakable-enterprise-product-activation'
	proj = angr.Project(binName, load_options={"auto_load_libs": False})

	input_size = 0x43; # Max length from strncpy of 67 bytes, see 0x4005ae.

	argv1 = angr.claripy.BVS("argv1", input_size * 8)

	initial_state = proj.factory.entry_state(args=["./unbreakable-enterprise-product-activation", argv1]) 
	print "symbolic bytes=" + str(initial_state.libc.buf_symbolic_bytes)
	initial_state.libc.buf_symbolic_bytes=input_size + 7 # Thanks to Christopher Salls (@salls) for pointing this out. 
                                                         # By default there's only 60 symbolic bytes, which is too small.

    # # For some reason if you constrain too few bytes, the solution isn't found. To be safe, I'm constraining them all.
	for byte in argv1.chop(8):
	    initial_state.add_constraints(byte >= ' ') # '\x20'
	    initial_state.add_constraints(byte <= '~') # '\x7e'
	    # Source: https://www.juniper.net/documentation/en_US/idp5.1/topics/reference/general/intrusion-detection-prevention-custom-attack-object-extended-ascii.html
	    # Thanks to Tom Ravenscroft (@tomravenscroft) for showing me how to restrict to printable characters.

	initial_path = proj.factory.path(initial_state)
	pathGroup = proj.factory.path_group(initial_state)

	# OPTION 1: keep exploring the binary until "Congrats" appears in the stdout 
	pathGroup.explore(find=lambda p: "Thank you - product activated!" in p.state.posix.dumps(1))

	# OPTION 2: explore until path hits where the thank you message is printed. 
	#pathGroup.explore(find=0x40083e, avoid=0x400850)
                        #  = puts 'ty'     = puts 'activation failure'
	
	found = pathGroup.found[0] 
	solution = found.state.se.any_str(argv1)
	return solution

if __name__ == '__main__':
	print("The solution is '" + OKBLUE + main() + ENDC + "'")



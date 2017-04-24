#! /usr/bin/python
# -*- coding: utf-8 -*-

import angr

p = angr.Project('crackme0x00a')

# Path groups let you manipulate multiple paths in a slick way. 
# Paths are organized into “stashes”, which you can step forward, 
# filter, merge, and move around as you wish. There are different 
# kinds of stashes, which are specified in Paths. 

# Get the object to explore the different path groups
pg = p.factory.path_group()

# keep exploring the binary until "Congrats" appears in the stdout 
pg.explore(find=lambda p: "Congrats" in p.state.posix.dumps(1))

# grab the state of the path once the condition above is set
s = pg.found[0].state

# print the program stdout dump at the state
print s.posix.dumps(1)

# set flag = to the data sent into the program
flag = s.posix.dumps(0)

print(flag)
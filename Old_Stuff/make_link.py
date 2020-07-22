# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:22:11 2019

@author: B E N
"""

#!/usr/bin/python

import os, sys

# Open a file
path = '/mnt/c/Users/benja/Documents/Programming/Python\ Projects/Suduko_Solver/' 
path1 = '/mnt/c/Users/benja/Documents/'
#n"C://Users//benja//Documents//Programming//Python Projects//Suduko_Solver//log//log.txt"

# Now create another copy of the above file.
dst = "/tmp/foo.txt"
os.link(path,path1)

print( "Created hard link successfully!!")
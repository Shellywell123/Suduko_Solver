# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 19:22:11 2019

@author: B E N
"""

#!/usr/bin/python

import os, sys

# Open a file
path = r'C:\Users\benja\Documents\Programming' 
#n"C://Users//benja//Documents//Programming//Python Projects//Suduko_Solver//log//log.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# Close opened file
os.close( fd )

# Now create another copy of the above file.
dst = "/tmp/foo.txt"
os.link( path, dst)

print( "Created hard link successfully!!")
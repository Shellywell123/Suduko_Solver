# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 22:41:45 2019

@author: B E N
"""
from suduko_importer import import_suduko
from suduko_maker import print_suduko,easy_suduko1,easy_suduko2,easy_suduko3,medium_suduko1
from suduko_solver import welcome,solve

welcome('1.00')
suduko = easy_suduko1#import_suduko('s01b.txt')
print_suduko(suduko)

solve(suduko,'','')

###############################################################################
        #To do List
###############################################################################
        
#col,row checker double checking (if full ;break)
#clean up
#colours
#fix more than 2 gap checker
#box matcher
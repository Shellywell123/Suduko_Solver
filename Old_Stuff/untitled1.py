# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 20:04:39 2019

@author: B E N
"""

d=[[1,2,3],[1,2,3],[1,2,3]]

def section_to_elements(suduko,num):
    """ """
    x = make_to_123(num)[0]
    y = make_to_123(num)[1]
    section = suduko[y][x]
    elements = section[0]+section[1]+section[2]
    return elements
    
print(a)
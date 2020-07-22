# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 19:53:34 2019

@author: B E N
"""

from python.suduko_maker import make_9x9,print_suduko
import numpy as np

def import_suduko(file):
    """ """
    path_to_gitrepo = '/mnt/c/Users/benja/Documents/Programming/Python Projects/Suduko_Solver/'
    path = path_to_gitrepo+'Sudukos_txt/'+file
    
    raw_content = open(path,'r').read()
    content1 = open(path,'r').read().replace(' ','').replace('0',' ')

    print(path)
    print(raw_content)
   
    content = []
    for n in range(0,len(content1)):
        content.append(content1[n])
    
    s1 = [content[0:3],content[10:13],content[20:23]]
    s2 = [content[3:6],content[13:16],content[23:26]]
    s3 = [content[6:9],content[16:19],content[26:29]]
    
    s4 = [content[30:33],content[40:43],content[50:53]]
    s5 = [content[33:36],content[43:46],content[53:56]]
    s6 = [content[36:39],content[46:49],content[56:59]]
    
    s7 = [content[60:63],content[70:73],content[80:83]]
    s8 = [content[63:66],content[73:76],content[83:86]]
    s9 = [content[66:69],content[76:79],content[86:89]]
    
    sections = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
    imported_suduko = make_9x9(sections)
    return imported_suduko
    
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 22:56:26 2019

@author: B E N
"""

# MAke a 3x3 ##################################################################


#numbers = [1,2,' ',4,5,6,7,8,9] 
#checks = [1,2,3,4,5,6,7,8,9]
#letters = ['a','b','c','d','e','f','g','h','i']
#   
#vline = '|'
#hline = ' -------------------------------------\n'    
#    
#elements = make_elements(numbers)
#print (elements)
#section = make_3x3(elements)
#print_section(section)
##print(elements)
#
#locations =check_if_missing(elements)[1]
#missing =check_if_missing(elements)[0]
#print('section is missing',missing,'@ locations',letters[locations],'+')
#
#check_if_complete(elements)
    
    

# MAke a 9x9 ##################################################################
#
#s1 = []
#s2 = []
#s3 = []
#s4 = []
#s5 = []
#s6 = []
#s7 = []
#s8 = []
#s9 = []

#n1 = [1,' ',3,4,5,6,7,8,9] 
#n2 = [1,' ',' ',4,5,6,7,8,9]
#n3 = [1,' ',3,4,5,6,7,8,9]
#n4 = [1,' ',3,4,5,6,7,8,9]
#n5 = [1,' ',3,4,5,6,7,8,9]
#n6 = [1,' ',3,4,5,6,7,8,9]
#n7 = [1,' ',3,4,5,6,7,8,9]
#n8 = [1,' ',3,4,5,6,7,8,9]
#n9 = [1,' ',3,4,5,6,7,8,9]

#sections = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
#count = 0

# make random section
#for s in sections:
#    random.shuffle(n1)
#    elements = make_elements(n1)
#    sections[count] = make_3x3(elements)
#    count+=1

#count =0
#
#for s in sections:
#    sections[count] = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
#    count+=1

#def make_elements(numbers):
#    """ """
#    a = []
#    b = []
#    c = []
#    d = []
#    e = []
#    f = []
#    e = []
#    g = []
#    h = []
#    i = []
#    
#    elements = [a,b,c,d,e,f,g,h,i]  
#    section_elements = []
#    random.shuffle(numbers)
#    
#    counter = 0
#    for element in elements:
#        elements[counter] = numbers[counter]
#        section_elements.append(elements[counter])
#        counter+=1
#    return section_elements

            
#def suduko_complete(suduko,report,report2):
#    """ runs all sub methods for completing suduko"""
#    changes = 0
#    log_entries = []
#
#    section,s_log = suduko_section_completer(suduko,report)
#    if section > 0:
#        changes = changes+section
#        log_entries.append(s_log)
#
#    rows,r_log = suduko_row_completor(suduko,report,report2)
#    if rows > 0:
#        changes=changes+rows
#        log_entries.append(r_log)
#
#    cols,c_log = suduko_col_completor(suduko,report,report2)
#    if cols > 0:
#        changes=changes+cols
#        log_entries.append((c_log))
#        
#    cn,cn_log = suduko_col_check_complete(suduko,report)
#    if cn > 0:
#        changes=changes+cn
#        log_entries.append(cn_log)
#        
#    rn,rn_log = suduko_row_check_complete(suduko,report)
#    if rn > 0:
#        changes=changes+rn
#        log_entries.append(rn_log) 
#        
#    return changes,log_entries
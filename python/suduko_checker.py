# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 16:42:17 2019

@author: B E N
"""
from python.suduko_actions import *
import numpy as np

###############################################################################
        # checks
###############################################################################

def check_if_missing(elements):
    """ """
    missing = []
    
    locations = []
    counts=0
    checks = [1,2,3,4,5,6,7,8,9]

    def remAll(L, item):
        answer = []
        for i in L:
            if i!=item:
                answer.append(i)
        return answer

    for num in checks:
        #print(elements)
        elements_int = [int(i) for i in remAll(elements,' ')]
        if num not in elements_int:

            missing.append(num)
        else:
            pass
        
        counts+=1
        if ' ' in elements:
            locations = np.where(np.array(elements) == ' ')
            
        else:
            locations = 'FULL'
            
    return missing,locations

        ###############################################################
        
def check_suduko_missings(suduko,report):
    """
     """
    sections_info = []
    for sec_num in range(1,10):
        section_info = []   
        elements = get_section_elements(suduko,sec_num)
        locations = check_if_missing(elements)[1]
        missing = check_if_missing(elements)[0]
        section_info.append(sec_num)
        section_info.append(missing)
        section_info.append(locations)        
        sections_info.append(section_info)        
        if report == 'print':
            if missing == []:
                print('section',sec_num,'is full')
            else:
                print('section',sec_num,'is missing',missing,'@ locations',locations,'+')
        else:
            pass
    return sections_info

        ###############################################################

def is_suduko_complete(suduko):
    """ checks if each section is complete, 
    if all sections complete, funtion returns True"""
    
    checks = check_suduko_missings(suduko,'')
    full_sections = 0
    for n in range(0,len(checks)):
        if checks[n][2] == 'FULL':
            full_sections=full_sections+1
            
    if full_sections == 9:
        return True

        ###############################################################
        
def unpack(suduko):
    """ 
    """
    elements = []
    for n in [0,1,2]:
        section = suduko[n]
        for m in [0,1,2]:
            subsection = section[m]
            for l in [0,1,2]:
                subrow = subsection[l]
                for k in [0,1,2]:
                    element = subrow[k]
                    elements.append(element)
    return elements

        ################################################################
        
def check_secs_correct(suduko):
    """ check 1 of each number in each section """
    elements = unpack(suduko)
 #   print(elements)
    num_count = []
    checks = [1,2,3,4,5,6,7,8,9]
    for n in range(0,len(checks)):
        
        count = []
        tally = np.where(elements == checks[n])
        count.append(checks[n])
        count.append(tally)
        num_count.append(count)
        
    return 'passed'
  #  print(num_count)

        ################################################################
 
def check_rows_correct(suduko):
    """ checks each row has one of each number"""
    log_entries = []
    fails = []
    checks = [1,2,3,4,5,6,7,8,9]
    
    for i in [0,1,2,3,5,6,7,8]:
        row=get_row(suduko,i,'')
     #   print(row)
        
        num_count = []
        
        for num in checks:
            count = []
            count.append(num)
            count.append(row.count(num))
            num_count.append(count)
        
        for n in range(0,len(num_count)):
            if  num_count[n][1] > 1:
                fails.append(num_count[n])
                log_entry=str('row {} has {} instances of the number {}').format(i+1,len(num_count[n]),num_count[n][0])
                log_entries.append(log_entry)
            else:
                pass
    if len(fails) == 0:
        return 'passed'
    else:
        return log_entries
    
        ################################################################

def check_cols_correct(suduko):
    """ checks each column has one of each number"""        
    log_entries = []
    fails = []
    checks = [1,2,3,4,5,6,7,8,9]
    
    for i in [0,1,2,3,5,6,7,8]:
        col=get_col(suduko,i,'')
     #   print(row)
        
        num_count = []
        
        for num in checks:
            count = []
            count.append(num)
            count.append(col.count(num))
            num_count.append(count)
        
        for n in range(0,len(num_count)):
            if  num_count[n][1] > 1:
                fails.append(num_count[n])
                log_entry=str('col {} has {} instances of the number {}').format(i+1,len(num_count[n]),num_count[n][0])
                log_entries.append(log_entry)
            else:
                pass
    if len(fails) == 0:
        return 'passed'
    else:
        return log_entries
        
        ################################################################
        
def check(suduko):
    """ """
    errors = []
    passes = 0
    
    secs = check_secs_correct(suduko)
    rows = check_rows_correct(suduko)
    cols = check_cols_correct(suduko)
    
    for n in [secs,rows,cols]:
        if n == 'passed':
            passes=passes+1
        else:
            errors.append(n)
            
    if passes==3:
        return True
    else:
        return errors   
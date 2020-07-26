
from python.suduko_conversions import *

def section_to_elements(suduko,num):
    """ """
    y = sec_num_to_coords(num)[0]   
    x = sec_num_to_coords(num)[1]
    section = suduko[y][x]
    elements = []
    for n in [0,1,2]:
        for m in range(0,3):
            elements.append(section[n][m])
    return elements

        ###############################################################
                
def get_section_elements(suduko,section):
    """ takes sec num 1-9 and returns elements as list"""
    y  = sec_num_to_coords(section)[0]
    x  = sec_num_to_coords(section)[1]
    
    elements = []
    for l in [0,1,2]:
        for k in [0,1,2]:            
            elements.append(suduko[y][x][l][k])    
    return elements

        ###############################################################

def get_col(suduko,col_num012,report):
    """ returns elements of a column given a col number in 012 format """
    col_num123 = col_num012 +1
    n = make_it_012x(col_num123)
    i = make_it_123x(col_num123)
    
    v_elements = []
    v_elements.append(get_section_elements(suduko,i)[n])          
    v_elements.append(get_section_elements(suduko,i)[n+3])
    v_elements.append(get_section_elements(suduko,i)[n+6])
    
    v_elements.append(get_section_elements(suduko,i+3)[n])
    v_elements.append(get_section_elements(suduko,i+3)[n+3])
    v_elements.append(get_section_elements(suduko,i+3)[n+6]) 
    
    v_elements.append(get_section_elements(suduko,i+6)[n])
    v_elements.append(get_section_elements(suduko,i+6)[n+3])
    v_elements.append(get_section_elements(suduko,i+6)[n+6])
    
    return v_elements

        ##############################################################

def get_col_num(section_num,sub_sum_num):
    """
    returns col num from secnum and sub index
    """
    if section_num in [1,4,7]:
        if sub_sum_num in [0,3,6]:
            return 1
        if sub_sum_num in [1,4,7]:
            return 2
        if sub_sum_num in [2,5,8]:
            return 3

    if section_num in [2,5,8]:
        if sub_sum_num in [0,3,6]:
            return 4
        if sub_sum_num in [1,4,7]:
            return 5
        if sub_sum_num in [2,5,8]:
            return 6

    if section_num in [3,6,9]:
        if sub_sum_num in [0,3,6]:
            return 7
        if sub_sum_num in [1,4,7]:
            return 8
        if sub_sum_num in [2,5,8]:
            return 9

        ################################################################


def get_row(suduko,row_num012,report):
    """ returns row elements, from row num in 012 format"""
    row_num123 = row_num012 +1
    n = make_it_036(row_num123)
    i = make_it_147_from_08(row_num012)
    
    h_elements = (
                  get_section_elements(suduko,i  )[n:n+3]+
                  get_section_elements(suduko,i+1)[n:n+3]+
                  get_section_elements(suduko,i+2)[n:n+3]
                  )

    return h_elements 

        ###############################################################



def get_row_num(section_num,sub_sum_num):
    """
    returns row num from secnum and sub index
    """
    if section_num < 3:
        if sub_sum_num <3:
            return 1
        if 3 <= sub_sum_num < 7:
            return 2
        if sub_sum_num >= 7:
            return 3

    if 3 <=section_num < 7:
        if sub_sum_num <3:
            return 4
        if 3 <= sub_sum_num < 7:
            return 5
        if sub_sum_num >= 7:
            return 6

    if section_num >= 7:
        if sub_sum_num <3:
            return 7
        if 3 <= sub_sum_num < 7:

            return 8
        if sub_sum_num >= 7:
            return 9

        ###############################################################

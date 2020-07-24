# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 23:22:10 2019

@author: B E N
"""
from python.suduko_maker import print_suduko
#from suduko_checker import check
import numpy as np

###############################################################################
        #Messages
###############################################################################
complete_message = """\n
 ###############################
 ##---------------------------##               
 ##     SUDUKO COMPLETE!      ##
 ##---------------------------##
 ###############################"""
 
failed_message ="""
 ###############################
 ##---------------------------##               
 ##      SUDUKO FAILED !      ##
 ##---------------------------##
 ###############################
 """
 
def welcome(version_num):
    """prints welcome asci"""
    print(("""
#############################################
#   _________         .___     __           #
#  /   _____/__ __  __| _/_ __|  | ______   #
#  \_____  \|  |  \/ __ |  |  \  |/ /  _ \  #
#  /        \  |  / /_/ |  |  /    <  <_> ) #
# /_______  /____/\____ |____/|__|_ \____/  #
#         \/           \/          \/       #
#   _________      .__                      #
#  /   _____/ ____ |  |___  __ ___________  #
#  \_____  \ /  _ \|  |\  \/ // __ \_  __ \ #
#  /        (  <_> )  |_\   /\  ___/|  | \/ #
# /_______  /\____/|____/\_/  \___  >__|    #
#          \/                      \/  {} #
#############################################  
""").format(str(version_num)))
    
###############################################################################
    #Log
###############################################################################
    
def write_log_file(log):
    """ """
    path_to_gitrepo = '/mnt/c/Users/benja/Documents/Programming/Python Projects/Suduko_Solver/'
    path = path_to_gitrepo + 'log/log.txt'

    file = open(path,'w') 
    for n in range(0,len(log)):
        if len(log[n])>1:
            for m in range(0,len(log[n])):
                if len(log[n][m])>1:
                    for l in range(0,len(log[n][m])):
                        file.write(str(log[n][m][l]))         
                        file.write('\n')
                
                else:
                    file.write(str(log[n][m]))         
                    file.write('\n')
        else:
            file.write(str(log[n]))         
            file.write('\n')
    file.close()  
    return path

   
###############################################################################
    #Conversions
###############################################################################
    

def make_it_123(number):
    """ 1-9 to 123"""
    if 0<=number<=3:
        return number
    if 4<=number<=6:
        return number-3
    if 7<=number<=9:
        return number-6 

        ###############################################################
        
def make_it_123x(number):
    """ 1-9 to 123"""
    if 0<=number<=3:
        return 1
    if 4<=number<=6:
        return 2
    if 7<=number<=9:
        return 3

        ###############################################################
            
def make_it_012(number):
    """0-8 to 012 """
    if 0<=number<=2:
        return number
    if 3<=number<=5:
        return number-3
    if 6<=number<=8:
        return number-6 

        ###############################################################
        
def make_it_147_from_08(number):
    """0-8 to 147"""
    
    if 0<=number<=2:
        return 1
    if 3<=number<=5:
        return 4
    if 6<=number<=8:
        return 7

        ###############################################################
        
def make_it_147_from_19(number):
    """1-9 to 147"""
    
    if 1<=number<=3:
        return 1
    if 4<=number<=6:
        return 4
    if 7<=number<=9:
        return 7

        ###############################################################
        
def make_it_036(number):
    """ """
    if number in [1,4,7]:
        return 0
    if number in [2,5,8]:
        return 3
    if number in [3,6,9]:
        return 6

        ###############################################################
        
def make_it_012x(number):
    """ """
    if number in [1,4,7]:
        return 0
    if number in [2,5,8]:
        return 1
    if number in [3,6,9]:
        return 2
    
###############################################################################
        #Section/coordniates conversion
###############################################################################
        
def sec_num_to_coords(section_num):
    """ takes a number 1-9 and gives coords in terms of 0,1,2 [y,x]"""
   # print(section_num)
    if section_num == 1:
        return  [0,0]
    if section_num == 2:
        return  [0,1]
    if section_num == 3:
        return  [0,2]
    if section_num == 4:
        return  [1,0]
    if section_num == 5:
        return  [1,1]
    if section_num == 6:
        return  [1,2]
    if section_num == 7:
        return  [2,0]
    if section_num == 8:
        return  [2,1]
    if section_num == 9:
        return  [2,2]

        ###############################################################
        
def coords_to_sec_num(coords):
    """ takes coords in terms of 0,1,2 [y,x] and gives a number 1-9  """
   # print(section_num)
    if coords == [0,0]:
        return  1
    if coords == [0,1]:
        return  2
    if coords == [0,2]:
        return  3
    if coords == [1,0]:
        return  4
    if coords == [1,1]:
        return  5
    if coords == [1,2]:
        return  6
    if coords == [2,0]:
        return  7
    if coords == [2,1]:
        return  8
    if coords == [2,2] :
        return 9

###############################################################################
    #CHECKS
###############################################################################

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
        
def check_suduko_missings(suduko,report):
    """ """
    
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
        
def suduko_section_completer(suduko,report):     
    """ """
    changes = 0
    data = check_suduko_missings(suduko,report)  
    log_entries = []
    for n in range(0,len(data)):
        one_data = data[n]
        sec_num = one_data[0]
        #print(sec_num,one_data)
        
        if len(one_data[1]) == 1:

            if check_if_missing(section_to_elements(suduko,sec_num))[1] == 'FULL':
                pass
                
            else:
             #   print(one_data)
                y = sec_num_to_coords(sec_num)[0]
                x = sec_num_to_coords(sec_num)[1]
                element_loc = check_if_missing(section_to_elements(suduko,sec_num))[1][0][0]+1
                y1 = sec_num_to_coords(element_loc)[0]
                x1 = sec_num_to_coords(element_loc)[1]
                suduko[y][x][y1][x1]=data[n][1][0]
                
                log_entry = ('section ' + str(data[n][0]) + ' autocompleted with number ' + str(data[n][1][0]))
                log_entries.append(log_entry)
                print(log_entry)
                print_suduko(suduko)
                changes=changes+1
                
    return changes,log_entries

###############################################################################
        # Row Processes
###############################################################################

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
        
def check_rows(suduko,report):
    """ """
    if report == 'print':
        print ('\nrow,missing nos,locs')
    else:
        pass
    count = 1
    total_info = []
    for i in [1,4,7]:
        for n in [0,3,6]:
            info = []
            h_elements = []
            h_elements = (get_section_elements(suduko,i)[n:n+3]+
                          get_section_elements(suduko,i+1)[n:n+3]+
                           get_section_elements(suduko,i+2)[n:n+3])

            check = check_if_missing(h_elements)
            
            if check[1] == 'FULL':
                if report == 'print':
                    print(count,'COMPLETE')
                else:
                    pass
            else:
                
                info.append(count)
                info.append(check)         
                total_info.append(info)
                if report == 'print':
                    print(count,check)
                else:
                    pass
            count +=1
    return total_info

        ###############################################################
        
def row_data_report(suduko,report,report2):
    """ """
    total_info = []
    row_data = check_rows(suduko,report2)
    if report == 'print':
        print('\nROW DATA\nrow no. section ( y , x ) possible vals')
    else:
        pass
    for n in range (0,len(row_data)):
        info = []
        row_num = row_data[n][0]
        missing_nums = row_data[n][1][0]
        missing_locs = row_data[n][1][1]

        for num in range(0,len(missing_locs[0])):
            col_num = missing_locs[0][num]
            
            false_y = row_num
            false_x = col_num + 1
            
            lil_x = make_it_123(false_x)-1
            lil_y = make_it_123(false_y)-1
            
            coords =[lil_y,lil_x]
            section_num = coords_to_sec_num(coords)
                        
            if report == 'print':
                print(row_num,'     ',section_num,'      (',row_num,',',col_num+1,')',missing_nums)
            else:
                pass
            coord = []
            coord.append(false_y)
            coord.append(false_x)
            info.append(coord)
            info.append(section_num)
            info.append(missing_nums)
            total_info.append(info)
    return total_info

        ###############################################################
        
def suduko_row_completor(suduko,report,report2):
    """ """
    log_entries = []
    row_data = row_data_report(suduko,report,report2)
    #print(row_data)
    changes = 0

    for n in range(0,len(row_data)):
        if len(row_data[n][2]) == 1:
            sec_num = row_data[n][1]
            last_num = row_data[n][2][0]
           
            false_x = row_data[n][0][1]            
            false_y = row_data[n][0][0]
            
            lil_x = make_it_123(false_x)-1
            lil_y = make_it_123(false_y)-1
            
            big_y = int(np.ceil(float(false_y/3)))-1
            big_x = int(np.ceil((float(false_x/3))))-1
            
            suduko[big_y][big_x][lil_y][lil_x] = last_num
            log_entry = ('row '+str(row_data[n][0][0])+' autocompleted with number '+ str(last_num))
            log_entries.append(log_entry)
            print(log_entry)
            print_suduko(suduko) 
            changes = changes+1
            
    return changes, log_entries

        ###############################################################
        
def suduko_row_check_complete(suduko,report):
    """ """
  #  print_suduko(suduko)
    row_data = check_rows(suduko,'print')#report)
    log_entries = []
    changes = 0
    #print(row_data)
   # print(len(row_data))
    
    for n in range(0,len(row_data)):
        row_num = row_data[n][0]-1
        row_missing_nums = row_data[n][1][0]
        row_missing_locs = row_data[n][1][1][0]
        #print('row_num,row_missing_nums,row_missing_locs')
       # print(row_num,row_missing_nums,row_missing_locs)
        
        if len(row_missing_locs) <=1:
            print('debug')
            break
        else:

            
            #for m in range(0,len(row_missing_locs)):
            # changed by ben recently 
            for m in range(0,1):
                #print(m)
                col_data = get_col(suduko,row_missing_locs[m],'print')#report)

                
                #print(' ',col_missing_locs[m],' - ',row_data)
                for l in range(0,len(col_data)):
                    matches = []
                    for k in range(0,len(row_missing_nums)):
                        if row_missing_nums[k] == col_data[l]:
                            number_matched = row_missing_nums[k]
                            col_matched = row_missing_locs[m]
                            matches.append([col_matched,number_matched])
                       #     print('match',number_matched,'row',row_matched+1)
                            if len(row_missing_locs)-len(matches)==1:
                         #       print('caught',col_missing_locs,matches)
                                for z in range(0,len(matches)):
                                    index = np.where(row_missing_locs == matches[z][0])[0][0]
                                    col_missing_locs_updated = np.delete(row_missing_locs,index)
                             #       print('caught',col_missing_locs_updated,matches)
                                    col_num = col_missing_locs_updated[0]
                                    number = matches[z][1]
                                    
                                    lil_x = make_it_123(col_num+1)-1
                                    lil_y = make_it_123(row_num+1)-1
                                    
                                    big_x = int(np.ceil(float((col_num+1)/3)))-1
                                    big_y = int(np.ceil((float((row_num+1)/3))))-1
                                    
                           #         print(big_y,big_x,lil_y,lil_x)
                                    suduko[big_y][big_x][lil_y][lil_x] = number
                                    print_suduko(suduko)
                                    log_entry = ('row '+str(row_num +1)+' filled with number '+ str(number) +' via '+str(len(matches))+' column block(s)')
                                    log_entries.append(str(log_entry))
                                    print(log_entry)
                                    changes = changes+1
                            else:
                                pass                             
                            
                        else:
                            pass
                
    return changes,log_entries


###############################################################################
        # Column Processes
###############################################################################

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

        ###############################################################
        
def check_cols(suduko,report):
    """ """
    if report =='print':
        print ('\ncolumn,missing nos,locs')
    else:
        pass
    count = 1
    total_info = []
    for i in [1,2,3]:
        for n in [0,1,2]:
            v_elements = []
            info = []

            v_elements.append(get_section_elements(suduko,i)[n])          
            v_elements.append(get_section_elements(suduko,i)[n+3])
            v_elements.append(get_section_elements(suduko,i)[n+6])
            
            v_elements.append(get_section_elements(suduko,i+3)[n])
            v_elements.append(get_section_elements(suduko,i+3)[n+3])
            v_elements.append(get_section_elements(suduko,i+3)[n+6]) 
            
            v_elements.append(get_section_elements(suduko,i+6)[n])
            v_elements.append(get_section_elements(suduko,i+6)[n+3])
            v_elements.append(get_section_elements(suduko,i+6)[n+6])
            
            check = check_if_missing(v_elements)
            if check[1] == 'FULL':
                if report == 'print':
                    print(count,'COMPLETE')
                else:
                    pass
            else:
                
                info.append(count)
                info.append(check)         
                total_info.append(info)
                if report == 'print':
                    print(count,check)
                else:
                    pass
            count +=1
    return total_info

        ###############################################################
        
def col_data_report(suduko,report,report2):
    """ """
    total_info = []
    section_index = [[1,2,3],[4,5,6],[7,8,9]]
    col_data = check_cols(suduko,report2)
    if report == 'print':
        print('\nCOL DATA\ncol no. section ( x , y ) possible vals')
    else:
        pass
    for n in range (0,len(col_data)):
        info = []
        col_num = col_data[n][0]
        missing_nums = col_data[n][1][0]
        missing_locs = col_data[n][1][1]    
        section_y = int(np.ceil(float(col_num/3)))
        for num in range(0,len(missing_locs[0])):
            row_num = missing_locs[0][num]

            
            section_x = int(np.ceil(float(row_num/3))) 
            section_num = section_index[section_y-1][section_x-1]
            if report == 'print':
                print(row_num,'     ',section_num,'      (',row_num,',',col_num,')',missing_nums)
            else:
                pass
            coord = []
            coord.append(col_num)
            coord.append(row_num+1)
            
            info.append(coord)
            info.append(section_num)
            info.append(missing_nums)
            total_info.append(info)
    return total_info

        ###############################################################
            
def suduko_col_completor(suduko,report,report2):
    """ """
    changes =0
    log_entries = []
    col_data = col_data_report(suduko,report,report2)
    for n in range(0,len(col_data)):
        if len(col_data[n][2]) == 1:
            y = col_data[n][0][1]
            
            x = col_data[n][0][0]
            section_x = int(np.ceil(float(x/3)))
            section_y = int(np.ceil(float(y/3)))

            suduko[section_y-1][section_x-1][make_it_123(y)-1][make_it_123(x)-1] = col_data[n][2][0]
            log_entry = ('column '+str(col_data[n][0][0])+' autocompleted with number '+ str(col_data[n][2][0]))
            log_entries.append(str(log_entry))
            print(log_entry)
 #           print(log_entries)
            print_suduko(suduko)
            changes = changes+1
            
    return changes,log_entries

        ###############################################################
        
def suduko_col_check_complete(suduko,report):
    """ """
  #  print_suduko(suduko)
    col_data = check_cols(suduko,report)
    log_entries = []
    changes = 0
   # print(col_data)
    for n in range(0,len(col_data)):
        col_num = col_data[n][0]-1
        col_missing_nums = col_data[n][1][0]
        col_missing_locs = col_data[n][1][1][0]
        
        if len(col_missing_locs) <=1:
            break
        else:
          #  print(col_num,col_missing_nums,col_missing_locs)
            #for m in range(0,len(col_missing_locs)):
            #changed by ben recently 
            for m in range(0,1):
                row_data = get_row(suduko,col_missing_locs[m],report)
                
              #  print(' ',col_missing_locs[m],' - ',row_data)
                for l in range(0,len(row_data)):
                    matches = []
                    for k in range(0,len(col_missing_nums)):
                        if col_missing_nums[k] == row_data[l]:
                            number_matched = col_missing_nums[k]
                            row_matched = col_missing_locs[m]
                            matches.append([row_matched,number_matched])
                       #     print('match',number_matched,'row',row_matched+1)
                            if len(col_missing_locs)-len(matches)==1:
                         #       print('caught',col_missing_locs,matches)
                                for z in range(0,len(matches)):
                                    index = np.where(col_missing_locs == matches[z][0])[0][0]
                                    col_missing_locs_updated = np.delete(col_missing_locs,index)
                             #       print('caught',col_missing_locs_updated,matches)
                                    row_num = col_missing_locs_updated[0]
                                    number = matches[z][1]
                                    
                                    lil_x = make_it_123(col_num+1)-1
                                    lil_y = make_it_123(row_num+1)-1
                                    
                                    big_x = int(np.ceil(float((col_num+1)/3)))-1
                                    big_y = int(np.ceil((float((row_num+1)/3))))-1
                                    
                           #         print(big_y,big_x,lil_y,lil_x)
                                    suduko[big_y][big_x][lil_y][lil_x] = number
                                    print_suduko(suduko)
                                    log_entry = ('column '+str(col_num +1)+' filled with number '+ str(number) +' via '+str(len(matches))+' row block(s)')
                                    log_entries.append(str(log_entry))
                                    print(log_entry)
                                    changes = changes+1
                            else:
                                pass
                        else:
                            pass
            
    return changes,log_entries


###############################################################################
        # Solve
###############################################################################


def solve(suduko,report,report2):
    """ runs all sub solve process through a loop"""
   
    
    import time
    start = time.process_time()
    
    
    total_changes = 0
    log = []
    for n in range(1,10):
        #print(n)
        changes = 0
        log_entries = []
    
        # level 1 checks
        section,s_log = suduko_section_completer(suduko,report)
        if section > 0:
            changes = changes+section
            log_entries.append(s_log)
    
        rows,r_log = suduko_row_completor(suduko,report,report2)
        if rows > 0:
            changes=changes+rows
            log_entries.append(r_log)
    
        cols,c_log = suduko_col_completor(suduko,report,report2)
        if cols > 0:
            changes=changes+cols
            log_entries.append((c_log))
            
        #level 2 checks
        cn,cn_log = suduko_col_check_complete(suduko,report)
        if cn > 0:
            changes=changes+cn
            log_entries.append(cn_log)
            
        rn,rn_log = suduko_row_check_complete(suduko,report)
        if rn > 0:
            changes=changes+rn
            log_entries.append(rn_log) 

        log.append(['Pass '+str(n)+'---------------------------'])
        log.append(log_entries)
        total_changes=total_changes+changes
        
        if changes == 0:
            if is_suduko_complete(suduko) == True:
                if check(suduko)== True:
                    print(complete_message)
                    break
                
                else:
                    log.append(['ERRORS '+'---------------------------'])
                    log.append(check(suduko))
                    print(failed_message)
                    break
                
                             
                     
            else:
                print(' No more can be done on this ver :(')
                break
            
        else:
            pass
    
    path = write_log_file(log)
    print((
            """
 REPORT
 ------
  - Completed in {} seconds 
  - Passes completed    {}
  - Numbers filled   {}/81
  - log file written to {} """
               ).format(
                       (time.process_time() - start),
                       int((len(log)/2)-1),
                       total_changes,
                       path )  )
    #    view_log = input("\n\n View Log ? (y/n)\n")
    #    if view_log == 'y':
    #        print(log)
    #    else:
    #        pass
    return 0

###############################################################################
        #
###############################################################################
        
def unpack(suduko):
    """ """
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

###############################################################################
    #Maintance section for testing new functions
###############################################################################


#from suduko_importer import import_suduko
#from suduko_maker import print_suduko,easy_suduko1,medium_suduko1
#
#welcome('1.00')
#
#suduko = easy_suduko1
#print_suduko(suduko)
#solve(suduko,'','')

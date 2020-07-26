# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 23:22:10 2019

@author: B E N
"""

from python.suduko_maker import print_suduko
from python.suduko_checker import *
from python.suduko_actions import *
from python.suduko_ascii import *
from python.suduko_conversions import *
import numpy as np

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
    #solvers
###############################################################################

def auto_section_completer(suduko,report):     
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
                
                print_suduko(suduko)
                print(log_entry)
                changes=changes+1
                
    return changes,log_entries

###############################################################################
        # Row Processes
###############################################################################

        
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
        
def auto_row_completor(suduko,report,report2):
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
        
def auto_row_completor_n(suduko,report):
    """ """
  #  print_suduko(suduko)
    row_data = check_rows(suduko,report)
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
                col_data = get_col(suduko,row_missing_locs[m],report)

                
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
            
def auto_column_completor(suduko,report,report2):
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
        
def auto_column_completor_n(suduko,report):
    """
    """

  #  print_suduko(suduko)
    col_data = check_cols(suduko,report)
    log_entries = []
    changes = 0
   # print(col_data)

    # cycles through each column
    for n in range(0,len(col_data)):
        col_num = col_data[n][0]-1
        col_missing_nums = col_data[n][1][0]
        col_missing_locs = col_data[n][1][1][0]
     #   print(col_num+1,'='*10,col_missing_nums)

        # if number of missing elements is one or less in a given col
        if len(col_missing_locs) <=1:
            break

        # if number of missing elements is more than one in a given col
        else:

             # iterates through each missing numer
            for k in range(0,len(col_missing_nums)):
                matches = []

                # itertes through each missing loaction of a given col
                for m in range(0,len(col_missing_locs)):
                #changed by ben recently 
                #for m in range(0,1):

                    # data for intersecting row with col missing gap
                    row_data = get_row(suduko,col_missing_locs[m],report)
                 #   print(' ',col_missing_locs[m],' - ',row_data)

                
                 #   print(col_missing_nums[k],row_data)
                    #iterates through each intersection row elemenent
                  #  for l in range(0,len(row_data)):
                        
                    
                  #  print(row_data[l],col_missing_nums[k])

                    if str(col_missing_nums[k]) in row_data:
                    #    print(col_missing_nums[k])
                        number_matched = col_missing_nums[k]
                        row_matched = col_missing_locs[m]
                        matches.append([row_matched,number_matched])
#                            print('match',number_matched,'row',row_matched+1)
                       # print('num of missing = ',len(col_missing_locs),', num of matches = ', len(matches))
                    
                    if len(col_missing_locs)-len(matches)==1:
                   # print(len(col_missing_locs))
                  #      print('hfgfcxg')
                 #       print('caught',col_missing_locs,matches)
                       # for z in range(0,len(matches)):
                       # print(len(matches))
                        index = np.where(col_missing_locs == matches[0][0])[0][0]
                        col_missing_locs_updated = np.delete(col_missing_locs,index)
                 #       print('caught',col_missing_locs_updated,matches)
                        row_num = col_missing_locs_updated[0]
                        number = matches[0][1]
                        
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
    #check_cols(suduko,'print')
        
    return changes,log_entries

        ###############################################################

def auto_section_completor_n(suduko,report):     
    """ """
    #report = 'print'
    changes = 0
    data = check_suduko_missings(suduko,report)  
    log_entries = []

    #print(data)

    for n in range(0,len(data)):
        #n is also secnum
        one_data = data[n]
        sec_num = one_data[0]
        missing_nums = one_data[1]
        missing_locs = list(one_data[2][0])


        if (len(missing_nums) == 2) and (len(missing_locs) == 2):
        #    print('  ---- ',sec_num)
            #print(missing_nums)
            for missing_num in missing_nums:
               # print(missing_num)

               # for missing_loc in missing_locs:
                #print('row ',get_row_num(sec_num,subindex))
                #print('col ',get_col_num(sec_num,subindex))
                col_num_1 = get_col_num(sec_num,missing_locs[0])
                row_num_1 = get_row_num(sec_num,missing_locs[0])

                block_rows_1  = get_row(suduko,row_num_1-1,report)
                block_cols_1  = get_col(suduko,col_num_1-1,report)
              #  print(missing_locs)
              #  print(missing_locs[1])
                col_num_2 = get_col_num(sec_num,missing_locs[1])
                row_num_2 = get_row_num(sec_num,missing_locs[1])

                block_rows_2  = get_row(suduko,row_num_2-1,report)
                block_cols_2  = get_col(suduko,col_num_2-1,report)
                
                input_ =False

                if str(missing_num) in block_cols_1:
                    if (str(missing_num) not in block_cols_2) and (str(missing_num) not in block_rows_2):
                   #     print('section {} has a block for number {} in col {}'.format(sec_num,missing_num,col_num_1))
                        #if num in block col put num in other free box
                        num_to_input = missing_num
                        input_location = missing_locs[1]
                        block_type = 'col'
                        input_ = True


                if str(missing_num) in block_cols_2:
                    if (str(missing_num) not in block_cols_1) and (str(missing_num) not in block_rows_1):
                     #   print('section {} has a block for number {} in col {}'.format(sec_num,missing_num,col_num_2))
                        #if num in block col put num in other free box
                        num_to_input = missing_num
                        input_location = missing_locs[0]
                        block_type = 'col'
                        input_ = True

                if str(missing_num) in block_rows_1:
                    if (str(missing_num) not in block_cols_2) and (str(missing_num) not in block_rows_2):
                     #   print('section {} has a block for number {} in col {}'.format(sec_num,missing_num,row_num_1))
                        #if num in block row put num in other free box
                        num_to_input = missing_num
                        input_location = missing_locs[1]
                        block_type = 'row'
                        input_ = True


                if str(missing_num) in block_rows_2:
                    if (str(missing_num) not in block_cols_1) and (str(missing_num) not in block_rows_1):
                     #   print('section {} has a block for number {} in col {}'.format(sec_num,missing_num,row_num_2))
                        #if num in block row put num in other free box
                        num_to_input = missing_num
                        input_location = missing_locs[0]
                        block_type = 'row'
                        input_ = True
                
                if input_ == True:
                 #   print(one_data)
                    y = sec_num_to_coords(sec_num)[0]
                    x = sec_num_to_coords(sec_num)[1]
                    element_loc = input_location+1
                    y1 = sec_num_to_coords(element_loc)[0]
                    x1 = sec_num_to_coords(element_loc)[1]

                    suduko[y][x][y1][x1]=num_to_input
                    
                    print_suduko(suduko)
                    log_entry = ('section ' + str(sec_num) + ' autocompleted with number ' + str(num_to_input)+' via '+block_type + ' block')
                    log_entries.append(log_entry)
                    print(log_entry)
                    changes=changes+1
                    break
                
    return changes,log_entries

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
        section,s_log = auto_section_completer(suduko,report)
        if section > 0:
            changes = changes+section
            log_entries.append(s_log)
    
        rows,r_log = auto_row_completor(suduko,report,report2)
        if rows > 0:
            changes=changes+rows
            log_entries.append(r_log)
    
        cols,c_log = auto_column_completor(suduko,report,report2)
        if cols > 0:
            changes=changes+cols
            log_entries.append((c_log))
            
        #level 2 checks
        section_n,s_log = auto_section_completor_n(suduko,report)
        if section_n > 0:
            changes = changes+section_n
            log_entries.append(s_log)

        rn,rn_log = auto_row_completor_n(suduko,report)
        if rn > 0:
            changes=changes+rn
            log_entries.append(rn_log) 

        #level n checks
        cn,cn_log = auto_column_completor_n(suduko,report)
        if cn > 0:
            changes=changes+cn
            log_entries.append(cn_log)

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
                print('No more can be done on this ver :(')
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

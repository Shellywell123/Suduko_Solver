
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
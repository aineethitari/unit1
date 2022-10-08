# my library is where I will put useful functions
def author()->str:
    return "Ainee"

def validate_int_input(prompt:str)->int: #user enter input check if the input is an integer if not function will return error
    '''
    This function asks the user for an input and validates that the input is an integer
    '''
    end_code = "\033[00m"
    red = "\33[0;31m"
    num = input(prompt)
    while not num.isdigit():
        num = input(f"{red}Error {prompt}{end_code}")
    return int(num)

def banner(msg:str)->str:
    width = 100
    header_line = "#"*width
    space_line = "#" + " "*(width-2) + "#"
    msg_line = "#" + msg.center(width-2) + "#"
    return header_line + "\n" + space_line + "\n" + msg_line + "\n" + space_line + "\n" + header_line

def average()->int:
    num_1 = validate_int_input("Please enter first number")
    num_2 = validate_int_input("Please enter second number")
    num_3 = validate_int_input("Please enter third number")
    return (num_1 + num_2 + num_3)/3

def calculate_balance(s)->int:
    with open (s) as file: #open file
        MANA_database = file.readlines()
    sum = 0
    for element in MANA_database:
        element_clean = element.strip()
        value = int(element_clean.split(",")[1])
        sum += value # add the element in each line together to calculate balance
    return sum

def validate_date(prompt:str)->str: #user will have to enter date in the correct format otherwise progra will return an error
    '''
    This function asks the user for an input and validate the input is a date in the format dd/mm/yy
    '''
    end_code = "\033[00m"
    red = "\33[0;31m"

    date = input(prompt)
    day = date[0:2] #the index that stores the date
    month = date[3:5] #index that stores month
    year = date[6:] #index that stores year

    while len(date)!=8: # if the date is not 8 then it's error
        date = input(f"{red}Error length Please re-enter the date in the format: dd/mm/yy{end_code}")
        day = date[0:2]
        month = date[3:5]
        year = date[6:]

    while (date[2] != "/" and date[5] != "/") and (not day.isdigit()) and (not month.isdigit()) and (not year.isdigit()): # the 3rd and 6th element needs to be a '/' and day,month,year needs to be integer
        date = input(f"{red}Error Please re-enter the date in the format: dd/mm/yy{end_code}")
        day = date[0:2]
        month = date[3:5]
        year = date[6:]

    return date

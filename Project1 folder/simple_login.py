# simple login function for login system
def simple_login(user:str,password:str)->bool: #input username and password and output true/false
    '''
    Simple authentification, needs file users.csv
    :param user: string
    :param password: string
    :return: True/False if user is in database
    '''
    with open("users.csv") as file: # eligible username and passwords are stored in this file
        database = file.readlines() # make file into a list
    output = False # set false as default
    for line in database: #check every line
        line_cleaned = line.strip() #remove\n
        user_pass = line_cleaned.split(",")
        if user == user_pass[0] and password == user_pass[1]: #check if the user entered the correct username and password
            output = True
            break

    return output

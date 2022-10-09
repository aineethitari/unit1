# MANA Crypto Wallet

![Mana decentraland](https://user-images.githubusercontent.com/112055062/194583498-f724d121-a418-4107-abe7-69a1692e21b1.png)

**Figure 1** The picture above shows the icon of the MANA coin used in Decentraland[1]

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all her transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution

I will design and make a digital ledger for a client who is Ms.Sato. The ledger will be about MANA which is a digital asset token used to pay for goods and sevices on Decentraland, a virtual world where users can buy, develop, and sell land [2]. 

## Rationale for the Proposed Solution:

I have chosen MANA as the currency for the client because MANA can be a good addition to the client's portfolio as the price movement of MANA is quite smooth and constant[3]. The financialisation of video gaming(GameFi)is also becoming more trendy these days. As MANA is used in Decentraland to buy assets and sell land, I encourage the client to explore the world of GameFi by using MANA.   

This ledger will be constructed using the software Python3. I have decided to use this software because of its simple syntax[4]. The straightforward language is very similar to English. Therefore, when there is a need to edit the functions, the developer will be able to do so easily. Moreover, Python3 is also commonly used for data analytics. Using Python3, datas can be collected, and organized safely. Lastly, as the main goal is to create digital wallet for the client, Python3 is also a great fit for finance in dealing with quantitative data. 

The data used in this wallet will be stored in a CSV file as they are simple and easy to use to store data. It is a plain text file, so using it to organize a big amount of data like the data in the client's wallet is a good fit.[5]

It will take approximately 3 weeks to make and will be evaluated according to the criteria below.

## Success Criteria
1. The electronic ledger is a text-based software (Runs in the Terminal).
2. The electronic ledger displays the basic description of the cyrptocurrency selected.
3. The electronic ledger allows to enter, withdraw and record transactions.
4. The electronic ledger displays MANA coverted to USD.
5. The electronic ledger allows the client to add a side note about her transactions. 
6. The electronic ledger allows the client to type the date and search for past transactions.

# Criteria B: Design

## System Diagram

![System Diagram for Ms Sato's Digital Ledger (2)](https://user-images.githubusercontent.com/112055062/194686052-dc1acd63-eaf2-4c57-b23a-2607df41a78a.jpg)

**Figure 2** This is the system diagram with starts from the input which is the keyboard to the output which is the terminal in Pycharm. The computer that is used to program this wallet is MacBook Pro 13-inch 2020(The specs are listed in the diagram) with macOS Monterey Version 12.4. The code is coded in Pycharm 20222.2.1. The data are recorded in comma separated value files. The first file, MANA_database.csv, stores the transactions. The second file, User_Note.csv, stores all the user's additional notes. The third file, users.csv, stores the usernames and passwords that are eligible to open the wallet. Python3.10 is used to code the wallet which 3 python files were used. Project1_Wallet is the python file for the main program. my_library is the file that stores functions from the validate integer input, the calculate balance and the validate date. simple_login is the file that includes the function to the login system. 

## Flow Diagrams

Login System

![simple login flowchart](https://user-images.githubusercontent.com/112055062/194010929-a551d6ab-b774-4920-b2d2-2d46d6ce22be.jpg)

**Figure 3** The flow diagram above shows the diagram of the login system. The login system is a function called simple_login which asks for inputs of the username and the password. Then the input of the username and the password is being compared to the list of usernames and passwords in a file called users.csv. The for loop is used to check every lines in users.csv. If the username entered matches the elements that records the username, and the password matches the password recorded in the list, the user entered the correct login information and can continue to the next section.

![calculate balance diagram (1)](https://user-images.githubusercontent.com/112055062/194599275-b6c5400f-e86d-45d5-beb9-44aa8fc907b3.jpg)

**Figure 4** The flow diagram above shows the operation of option 6 from the menu which allows the user to enter a date and the program will search for the date in a csv file called MANA_database.csv which records all the transactions made and the date. The program will read the file then look for the date that matches with the element on the list in the file. Then it prints out the list of transactions that was made on that day.  

![Option 2](https://user-images.githubusercontent.com/112055062/194602180-870beda6-db90-4dc9-b5e5-12a0f01f932d.jpg)

**Figure 5*** The flow diagram above shows the process in recording the deposit of the MANA coin. The program starts with asking for two inputs which are the amount that the user want to deposit and the date of the transaction. Then the file MANA_database.csv is used to record the new information that the user had entered. The program then return a message confirming the user that they have entered the information successfully. Lastly, the program asks the user whether they want to know the total balance of the MANA coin in the wallet. 

## Test Plan

| Description | Type | Inputs | Outputs | 
| ----------- | ---- | ------ | ------- |
|Login system |White box, integration test, functional | 1. Enter the username 2.Enter password | If the user entered the correct username and password, the program will continue to the next page. If the user entered the wrong username and password, the program will print: Wrong password and username. Please enter again.|
|User password database check| unit test, functional| 1. Open username and password section on the file: users.csv 2.Check that each lines contain a value with two elements separated by commas| If the users usernames and passwords are listed in the correct format, the passwords will match.|
|Menu check|Unit test, White box, functional| 1.Enter the option number of all the 6 options available 2.Enter a wrong number outside of the six options | If the number entered is within the 6 options available, the program should continue to the options chosen. If the number entered is the incorrect number, the program should return "8 is in correct. Please enter an option [1-6]".|
|Validate date|Unit test, functional| 1. Check if the program tells the user the correct format of date to input 2. Enter the date in the correct format 3. Enter the date in incorrect format 4. Try to re-enter in correct format | If the input is in correct format, the program should continue to the next step. If the input is in the wrong format, the program should return a message informing the user that it is incorrect and please re-enter. |
|Test option 1: description of MANA| integration unit test, functional| 1.Enter option 1 in the menu | The program shows the description of the MANA coin|
|Test option 2: record deposit and show balance| unit test, functional| 1.Enter option2 2.Enter amount of money to deposit 3.Enter the date 4.Show balance| When asked to enter amount of money, if enter an integer, the program then asks for date. If enter date, then show a message saying that the transaction has been recorded and shows the total balance.|
|Test option 3: record withdrawal and show balance| unit test, functional| 1. Enter option 3 2.Enter amount of money to withdraw 3.Enter the date 4.Show baance|When asked to enter amount of money, if enter an integer, the program then asks for date. If enter date, then show a message saying that the transaction has been recorded and shows the total balance.|
|Test option 4: Convert MANA balance to USD| Unit test, functional| 1.Enter option 4| The program will show the balance and the amount in USD|
|Test option 5: option for users to record their notes | Unit test, functional| 1. Enter option 5 2.Enter date 3.Enter note 4.enter 'yes' to see past notes| If enter wrong date, the program asks to enter date again. If enter correct date, the program continues to the next section. After enter note, the program asks if user would like to see past notes. If answer no, the program returns to menu. If enter yes, the program shows  all the notes and the dates entered.|
|Test option 6: search for translation| Unit test, functional|1.Enter option 6 2.Enter the date in the correct format | If the date is the date that the user have put in the notes before, the note will show. If not the program will return back to the menu.|
|Edit the aesthetics of the interface| integration, non-functional| 1.Run every section of the program 2.Edit the colors and spacings| The printed parts looks understandable and beautiful|
|Test by users| Integration, Blackbox, Functional| 1.Users use the program as if they were the client 2.Test with no prior knowledge of how the program works| If the users understood what to input in each section, the program will return an output. The output should be what the users are looking for. |
|Feedback from users| Non-functional, usability| 1.Input all the information required or each section| Users are able to use if it is a friendly and not an over complicated program.
|End to End Test| System Testing| 1.Try all the functions from start to the end| The program works smoothly with no problems|

**Table 1** The test plan shows how the program has been tested. The types of tests that are implemented are Unit Testing, Integration, and System Testing. The input in the table is the steps to follow in testing the functions and the output is what the program should return in the test. The test also include white box testing which is done by the developer who knows the code behind the program and black box testing done by other people who do not know the code. 

## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Create system diagram                                         | To have a clear idea of the hardware and software requirements for the proposed solution                        | 10min         | Sep 22                 | B         |
| 2       | Design success criteria                                      | To plan the functions of the ledger.                         | 20min         | Sep 23                 | A         |
| 3       | Meet with the client to discuss the success criteria for approval                                   | To make sure the client is on the same page with the designer and have an agreement on the functions of the ledger.            | 10min         | Sep 23                 | A         |
| 4       | Created a flow diagram for login system                                    | To illustrate a picture of how the login system works and plan before coding              | 10min         | Sep 27                 | B         |
| 5       | Coded the login system with username and user's password                                   | To have a secure system and not to let any of the user's information leaked out            | 50min         | Sep 27                 | C         |
| 6       | Tested the login system with several usernames and passwords                                   | To make sure the login system works            | 5 min         | Sep 27                 | B         |
| 7       | Coded the menu                                   |To let the user select the options of the program         | 30 min         | Oct 02                 | C         |
| 8       | Tested the menu manually with white box method by the developer   |To make sure the menu functions and each options can be used         | 5 min         | Oct 02                 | B         |
| 9      | Coded the option 2: Record MANA deposit and show total balance                               |To allow users to find a place to store there value of MANA.      | 1 hour         | Oct 02                 | C         |
| 10       | Tested option 2 manually with white box method by the developer                              |To make sure MANA coins can actually be added to the wallet and the total balance is correct       | 10 min         | Oct 02                 | A         |
| 11      | Coded function to validate user's transaction date.                                |Users can keep track of the date they have made the transaction       | 1 hour         | Oct 02                 | C         |
| 12      | Tested  validate user's transaction date function manually with white box method by the developer                                  |Make sure that the dates input by the users are eligible       | 20 min         | Oct 02                 | B         |
| 13      | Coded option number 4: Convert MANA balance to USD                                |Users know can compare the MANA value to a universally familiarized currency.      | 30 min         | Oct 04                 | C         |
| 14      | Tested option number 4: Convert MANA balance to USD manually with white box method by the developer                              |The actual balance in the user's wallet is converted to USD      | 10 min         | Oct 04                 | B         |
| 15      | Coded option number 3: Record MANA withdrawal and show total balance                                |Users can record the value they have without having to calculate manually by hand      | 1 hour         | Oct 04                 | C         |
| 16      | Tested option number 3: Record MANA withdrawal and show total balance manually with white box method by the developer                               |The withdrawal is put into the database correctly and the balance is calculated correctly     | 10 min     | Oct 04                 | B         |
| 17     | Tested menu options 1-5 grey box testing method by peers who has some knowledge of python|The function is reviewed by another person with some coding knowledge     | 10 min         | Oct 05                 | B         |
| 18     | Coded option number 5: User notes                                |Users can record any notes they want to put on with the dates to keep track of what is going on      | 1 hour         | Oct 05                 | C         |
| 19      | Update some of the errors in the functions such as the Validate date function      |Make sure there will be no errors      | 2 hr         | Oct 05                 | C         |
| 20      | Tested the functions with a senior with python knowledge usin the grey box method   |Make sure the functions are understandable and works efficienly     | 20 min         | Oct 06                 | B         |
| 21      | Add elaborated explanations on the reasons why the developer chooses the MANA crypto currency and why the developer chooses Python to develop the program.  |To help the clients understand the purpose behind the decisions made.    | 20 min         | Oct 06                 | A         |
| 22      | Functional test with multiple users and receive feedback |To make sure users would understand how to use the wallet    | 30 min         | Oct 07                 | B         |
| 23      | Coded option 6: use date to search for transaction |Users can check what transaction was made in each date   | 2 hr         | Oct 07                 | C         |
| 23      | Added the code for the users to return to menu once they have used a function |Users do not need to re-login or run the program again if they want to use another function   | 1 hr         | Oct 07                 | C         |
| 24      | Decorated the program to make the printed looks nice and colorful | Aesthetically appealing interface for users   | 1 hr         | Oct 07                 | C         |
| 25      | Finish the system diagram | Make sure the clients understand the system behind the wallet | 30 min      | Oct 07                 | B         |
| 26      |Write the description of the flowchart in figure 2 | Guide the client to understand how the flowchart works | 10 min      | Oct 07                 | B         |
| 27      | Create a flowchart for option 6: enter date and search for transaction  | Show the users how the program works in a clearer way | 20 min      | Oct 07                 | B         |
| 28      | Create a flowchart for option 2: user record transaction and show total balance |To let the users know how the program was created | 30 min      | Oct 07                 | B         |
|29|Complete test plan table| To show the client that the function works and has been tested multiple times| 2 hr | Oct 08| B

**Table 2** This table shows the record of tasks from the begining of creating this wallet until the end when the wallet is completed. The table consists of the task number, planned action, planned outcome, the time taken to do the task, the date, and the criterion of the task(A,B,C).

# Criteria C: Development

## Login System

```.py
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
```

**Figure 6** The figure show the Login System of the wallet. The login system is a function called simple_login which recieves inputs of the username and the password, then returns True or False. The program opens the file users.csv which stores the usernames and passwords which are eligible to open the wallet. Then the usernames and passwords in the file is compared to what the user enters.

```.py
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
```

**Figure 7** The code shows the function that validate the user's date input to be in the format dd/mm/yy. The function ensures that the input is within the length of 8. Then it make sures that the 3rd and the 6th element of the input is a "/". Then it makes sure that the day month and year entered are digits. With all of these limitations, the user would only be able to enter a date in the correct format.

```.py
color = ["\33[0;30m", "\33[0;31m", "\33[0;32m", "\33[0;34m", "\33[0;35m"]# ascii colors
end_code = "\033[00m" #use after every color

print(f"""{color[4]}
▒█▀▄▀█ ░█▀▀█ ▒█▄░▒█ ░█▀▀█ 　 ▒█░░▒█ █▀▀█ █░░ █░░ █▀▀ ▀▀█▀▀ 
▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ 　 ▒█▒█▒█ █▄▄█ █░░ █░░ █▀▀ ░░█░░ 
▒█░░▒█ ▒█░▒█ ▒█░░▀█ ▒█░▒█ 　 ▒█▄▀▄█ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░{end_code}""")
login_msg = f"{color[3]}This is the login page of your MANA wallet{end_code}"
print(login_msg) #intro before enter username password
user = input(f"{color[4]}Please enter username{end_code}")
password = input(f"{color[4]}Please enter password{end_code}")
```

**Figure 8** The code shows the code of the first page that is printed on the terminal. An ascii text art[6] is showed in colors from ascii color codes[7]. 

```.py
def calculate_balance(s)->int:
    with open (s) as file: #open file
        MANA_database = file.readlines()
    sum = 0
    for element in MANA_database:
        element_clean = element.strip()
        value = int(element_clean.split(",")[1])
        sum += value # add the element in each line together to calculate balance
    return sum
```

**Figure 9** The figure shows the function for calculating the total balance of the wallet. The function open and reads the file then add the amount together using the for loop function. 

## Whole Code

```.py
# main code for wallet
import csv

from my_library import validate_int_input,calculate_balance,validate_date #import function from library
from simple_login import simple_login # for login system

color = ["\33[0;30m", "\33[0;31m", "\33[0;32m", "\33[0;34m", "\33[0;35m"]# ascii colors
end_code = "\033[00m" #use after every color

print(f"""{color[4]}
▒█▀▄▀█ ░█▀▀█ ▒█▄░▒█ ░█▀▀█ 　 ▒█░░▒█ █▀▀█ █░░ █░░ █▀▀ ▀▀█▀▀ 
▒█▒█▒█ ▒█▄▄█ ▒█▒█▒█ ▒█▄▄█ 　 ▒█▒█▒█ █▄▄█ █░░ █░░ █▀▀ ░░█░░ 
▒█░░▒█ ▒█░▒█ ▒█░░▀█ ▒█░▒█ 　 ▒█▄▀▄█ ▀░░▀ ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░{end_code}""")
login_msg = f"{color[3]}This is the login page of your MANA wallet{end_code}"
print(login_msg) #intro before enter username password
user = input(f"{color[4]}Please enter username{end_code}")
password = input(f"{color[4]}Please enter password{end_code}")
password_correct = simple_login(user=user,password=password)

if password_correct == True:
    go_menu = 1
    while go_menu == 1:

        menu = f"""{color[3]}
        1. Description of MANA cryptocurrency
        2. Record MANA deposit and show total balance
        3. Record MANA withdrawal and show total balance
        4. Convert MANA balance to USD 
        5. My notes
        6. Search for transaction{end_code}
        """
        print("""
        """)
        print(f"{color[3]}Menu".center(50))
        print(menu)

        option = validate_int_input(f"{color[4]}Please enter an option [1-6]{end_code}")
        while option not in [1,2,3,4,5,6]:#make sure the user input only 1-6
            option = validate_int_input((f"{color[1]}{option} is in correct.{end_code} Please enter an option [1-6]"))

        if option == 1: #show description of mana
            description = f"""
    {color[4]}MANA is a cryptocurrency that facilitates purchases of LAND, and goods and services used in Decentraland.{end_code}
    {color[3]}Now...what is LAND and Decentraland?{end_code}
    {color[4]}LAND is an NFT that is used to mark the ownership of land in digital real estate.{end_code} 
    {color[3]}Decentraland is a virtual reality world where users can buy and sell digital real estate, while interacting with other users in the virtual world.{end_code} """
            print(description)
            go_menu = validate_int_input(f"""
    {color[4]}Enter 1 if you would like to return to the main menu, or enter 2 if you would like to exit{end_code}""")


        if option == 2:#record deposit and show balance
            amount = validate_int_input(f"{color[3]}Please enter the MANA amount you would like to deposit{end_code}") #amount of money to deposit
            date = validate_date(f"{color[4]}Please enter the date of your transaction in dd/mm/yy format (ex: 02/10/22){end_code}") #validate it later
            file = open("MANA_database.csv","a")
            file.writelines([f"{date},{amount}\n"]) #add new value to file
            file.close()
            print(f"{color[3]}Congratulations!{end_code} You have successfully recorded your transaction.") #confirmation message
            balance = calculate_balance(s="MANA_database.csv")
            balance_msg = f"Your total balance is {color[4]}{balance}{end_code}."
            print(balance_msg)
            go_menu = validate_int_input(f"""
    Enter 1 if you would like to return to the main menu, or enter 2 if you would like to exit""")


        if option == 3: #record withdrawal and show balance
            amount = validate_int_input(f"{color[3]}Please enter the MANA amount you would like to withdraw{end_code}")
            amount = amount*(-1) #turn input into negative for withdrawal
            date = validate_date(f"{color[4]}Please enter the date of your transaction in dd/mm/yy format (ex: 02/10/22){end_code}")
            file = open("MANA_database.csv", "a")
            file.writelines([f"{date},{amount}\n"]) #add amount to file
            file.close()
            print(f"{color[3]}Congratulations!{end_code} You have successfully recorded your transaction.")
            balance = calculate_balance(s="MANA_database.csv")
            balance_msg = f"Your total balance is {color[4]}{balance}{end_code}."
            print(balance_msg) #show balance
            go_menu = validate_int_input(f"""
    Enter 1 if you would like to return to the main menu, or enter 2 if you would like to exit""")

        if option == 4: #show balance in USD
            balance = calculate_balance(s="MANA_database.csv") #get balance from file and calculate_balance function
            balance_in_USD = balance * 0.697249 # Convert by multi[lying 0.697249
            print(f"Your balance is {color[4]}{balance}{end_code} MANA, which is {color[4]}{balance_in_USD}{end_code} USD")
            go_menu = validate_int_input(f"""
    Enter 1 if you would like to return to the main menu, or enter 2 if you would like to exit""")

        if option == 5: #add note and date
            note_date = validate_date(f"{color[3]}Welcome to your personal notebook. Please enter your date in dd/mm/yy format (ex: 02/10/22){end_code}")
            note = input(f"{color[4]}Feel free to enter your notes{end_code}")
            file = open("User_Note.csv","a") #file to store user notes
            file.write(f"{note_date},{note}\n") #write the new note into the file
            print(f"{color[3]}Congratulations!{end_code} You have successfully recorded your transaction.") #confirmation note
            file.close()
            show = input(f"{color[4]}If you wish to see your past notes, please enter 'yes', or else please enter 'no'{end_code}")
            if show == "yes":
                with open("User_Note.csv", 'r') as f: #reopen file
                    lines = f.read().split('\n') #show notes
                f.close()
                for line in lines:
                    print(line)
            go_menu = validate_int_input(f"""{color[3]}
    Enter 1 if you would like to return to the main menu, or enter 2 if you would like to exit{end_code}""")

        if option == 6: # search for transaction with date
            search_date = validate_date(f"{color[3]}Please enter the date you wish to search in the format dd/mm/yyy{end_code} ")
            with open('MANA_database.csv','r') as read_obj:
                reader = csv.reader(read_obj)
                list_of_csv = list(reader) # the list of the whole csv file
                num_list = len(list_of_csv) # length of the list of csv file
                for i in  range(num_list): #match the csv file with the date that is entered
                    if search_date == list_of_csv[i][0]:
                        msg = f"On the date {list_of_csv[i][0]}, you deposited/withdrawed {list_of_csv[i][1]}"
                        print(msg)
            go_menu = validate_int_input(f"""{color[3]}
    Enter 1 if you would like to return to the main menu, or enter 2 if you would like to exit{end_code}""")

    if go_menu == 2:
        print(f"""
        Thank you for using MANA wallet. See you again next time""")
else:
    print(f"{color[1]}Wrong password and username. Please enter again.{end_code}")
    exit()
```
**Figure 9** This is the code for Project1_Wallet.py

```.py
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
```

**Figure 10** This is the code for simple_login.py

```.py
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
```

**Figure 11** This is the code for my_library.py

## Video

[Video Test ](https://drive.google.com/file/d/1g3GjzH9FRwfJ89Aeswn6jBu_IlZPwZqI/view?usp=sharing)

## Citation
[1] Binance Academy. “What Is Decentraland (Mana)?” Binance Academy, Binance Academy, 18 Nov. 2021, https://academy.binance.com/en/articles/what-is-decentraland. 

[2] “Decentraland Price, Chart, &amp; Supply Details - Mana Price.” Gemini, https://www.gemini.com/prices/decentraland. 

[3] “Decentraland (Mana) Price Prediction 2021&nbsp;2022&nbsp;2023-2040.” Changelly.com, 6 Oct. 2022, https://changelly.com/blog/decentraland-mana-price-prediction/. 

[4] FutureLearn. “What Is Python Used for?: 10 Practical Python Uses.” FutureLearn, 30 Dec. 2021, https://www.futurelearn.com/info/blog/what-is-python-used-for. 

[5]“What Is a .CSV File and What Does It Mean for My Ecommerce Business?” BigCommerce, https://www.bigcommerce.com/ecommerce-answers/what-csv-file-and-what-does-it-mean-my-ecommerce-business/. 

[6] “ASCII Text Art Generator.” Symbols, https://fsymbols.com/generators/carty/. 

[7] drPinzonISAK. “Unit1_g1/ASCI_COLORS.MD at Main · Drpinzonisak/UNIT1_G1.” GitHub, 14 Sept. 2022, https://github.com/drPinzonISAK/unit1_g1/blob/main/ASCI_colors.md. 


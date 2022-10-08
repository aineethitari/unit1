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

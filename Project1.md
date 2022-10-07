# Crypto Wallet

![](22ROOSE-master768.gif)  
<sub>Illustration for Glenn Harvey</sub>

# Criteria A: Planning

## Problem definition

Ms. Sato is a local trader who is interested in the emerging market of cryptocurrencies. She has started to buy and sell electronic currencies, however at the moment she is tracking all his transaction using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Ms Sato to find past transactions or important statistics about the currency. Ms Sato is in need of a digital ledger that helps her track the amount of the cryptocurrency, the transactions, along with useful statistics. 

Apart for this requirements, Ms Sato is open to explore a cryptocurrency selected by the developer.

## Proposed Solution

I will design and make a digital ledger for a client who is Ms.Sato. The ledger will be about MANA which is a digital asset token used to pay for goods and sevices on Decentraland, a virtual world where users can buy, develop, and sell land [1]. 

## Rationale for the Proposed Solution:

I have chosen MANA as the currency for the client because MANA can be a good addition to the client's portfolio as the price movement of MANA is quite smooth and constant[2]. The financialisation of video gaming(GameFi)is also becoming more trendy these days. As MANA is used in Decentraland to buy assets and sell land, I encourage the client to explore the world of GameFi by using MANA.   

This ledger will be constructed using the software Python3. I have decided to use this software because of its simple syntax[3]. The straightforward language is very similar to English. Therefore, when there is a need to edit the functions, the developer will be able to do so easily. Moreover, Python3 is also commonly used for data analytics. Using Python3, datas can be collected, and organized safely. Lastly, as the main goal is to create digital wallet for the client, Python3 is also a great fit for finance in dealing with quantitative data. 

The data used in this wallet will be stored in a CSV file as they are simple and easy to use to store data. It is a plain text file, so using it to organize a big amount of data like the data in the client's wallet is a good fit.[4]

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
![System Diagram for Ms Sato's Digital Ledger](https://user-images.githubusercontent.com/112055062/194578905-70a24809-1be2-4b4f-9aa8-03e88e8348d4.jpg)

## Flow Diagrams

Login System

![simple login flowchart](https://user-images.githubusercontent.com/112055062/194010929-a551d6ab-b774-4920-b2d2-2d46d6ce22be.jpg)

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
| 21      | Add elaborated explanations on the reasons why the developer chooses the MANA crypto currency and why the developer chooses Python to develop the program.  |To help the clients understand the purpose behind the decisions made.    | 20 min         | Oct 07                 | A         |


# Criteria C: Development

## Login System

```.py
def simple_login(user:str,password:str)->bool:
    '''
    Simple authentification, needs file users.csv
    :param user: string
    :param password: string
    :return: True/False if user is in database
    '''
    with open("users.csv") as file:
        database = file.readlines()
    output = False
    for line in database:
        line_cleaned = line.strip() #remove\n
        user_pass = line_cleaned.split(",")
        if user == user_pass[0] and password == user_pass[1]:
            output = True
            break

    return output
```

Image of the login system

<img width="1124" alt="Login system" src="https://user-images.githubusercontent.com/112055062/193435730-fe22a5f1-355c-4304-9596-9c33cd77372d.png">

## Citation

[1] “Decentraland Price, Chart, &amp; Supply Details - Mana Price.” Gemini, https://www.gemini.com/prices/decentraland. 

[2] “Decentraland (Mana) Price Prediction 2021&nbsp;2022&nbsp;2023-2040.” Changelly.com, 6 Oct. 2022, https://changelly.com/blog/decentraland-mana-price-prediction/. 

[3] FutureLearn. “What Is Python Used for?: 10 Practical Python Uses.” FutureLearn, 30 Dec. 2021, https://www.futurelearn.com/info/blog/what-is-python-used-for. 

[4]“What Is a .CSV File and What Does It Mean for My Ecommerce Business?” BigCommerce, https://www.bigcommerce.com/ecommerce-answers/what-csv-file-and-what-does-it-mean-my-ecommerce-business/. 

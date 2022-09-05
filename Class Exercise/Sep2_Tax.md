# Class exercise from September 2nd 2022
Create a program that calculates the tax for a salary entered by the user following the table below

```.py
salary = int(input("Please enter your salary "))

if salary<=10000:
    tax = salary*(5/100)

if salary>=10001 and salary<=50000:
    tax = salary*(10/100)

if salary>=50001 and salary<=100000:
    tax = salary*(15/100)

if salary>=100001:
    tax = salary*(25/100)

print(tax)
```

<img width="1203" alt="Tax Pycharm" src="https://user-images.githubusercontent.com/112055062/188482064-d38ea82c-0374-4741-a2f8-7834e50ff251.png">

**Fig.1** Working from Pycharm

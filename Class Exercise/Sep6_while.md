# 6th September 2022 - While loop
## Using while loop create a counter that counts from 0 to input

```.py
number = input("Please enter a positive number ")

while not number.isdigit():
    number = input("Please enter value again. The value entered is not a number ")

number = int(number)

starting_point = 0
while starting_point < number:
    starting_point = starting_point + 1
    print(starting_point)
```



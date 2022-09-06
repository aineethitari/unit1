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

<img width="748" alt="while loop pycharm" src="https://user-images.githubusercontent.com/112055062/188628975-20427125-410a-4046-b47f-c03ee3eaae58.png">

**Fig.1** Code from pycharm

## Using while loop create a counter that counts from input of start to end with steps 

```.py
start = (input("Please enter starting number "))
end = (input("Please enter ending number "))
step = (input("Please enter the interval between each number"))

while not start.isdigit():
    start = input("Your previous starting number is invalid. Please enter another starting number.")

while not end.isdigit():
    end = input("Your previous ending number is invalid. Please enter another ending number. ")

while not step.isdigit():
    step = input("Your previous interval number is invalid. Please enter another interval number. ")

start = int(start)
end = int(end)
step = int(step)
```

<img width="955" alt="while loop step pycharm" src="https://user-images.githubusercontent.com/112055062/188629712-e037c104-cbda-435d-b1fa-9a19bca6a85c.png">

**Fig.2** Image of the code from pycharm

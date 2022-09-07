# Quiz 004
## The following flow diagram contains bad coding practices, improve it, then test it with the following inputs:

![Quiz004edited_flowchart](https://user-images.githubusercontent.com/112055062/188648912-0ae262d6-7abf-44e1-9581-2d420ca7e4c8.jpeg)

**Fig.1** Flow chart of the improved code with proper coding practices

## What is the intended purpose of this program?
The purpose of this program is the print the last digit of the integer on the unit + the last digit of the integer on the tenths.

## HL: Code the program

```.py
num_1 = int(input("Enter a number "))

d_1 = num_1 % 10
d_2 = int(num_1/10)

if num_1 != d_1 + d_2:
    print("Perfect")

else:
    print("No perfect")

exit()
```

<img width="1134" alt="Quiz004 pycharm" src="https://user-images.githubusercontent.com/112055062/188869215-fe418850-1b9a-4f8a-a339-87ba0ce98d82.png">

**Fig.1** The image of the code from pycharm

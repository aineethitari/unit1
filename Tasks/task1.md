# Task 1
**Task 1.1** Create a program and the flow diagram that shows the colors of all the lockers from 1 to 2400

```.py
total_num = 10
for locker_num in range(1, total_num+1, 1):
    print(f"The locker number is {str(locker_num)}")
    number_group = (locker_num-1) % 4
    print(f"Number group is {number_group}")
    if number_group == 0:
        print(f"The color is red")
    if number_group == 1:
        print(f"The color is white")
    if number_group == 2:
        print(f"The color is yellow")
    if number_group == 3:
        print(f"The color is blue")
```

**Task2** Using the program above, create another program that allows the user to enter a number and the program outputs the color that should be used in the locker.

```.py
locker_num = int(input("Please enter a locker number ID from 1-2400"))
number_group = (locker_num - 1) % 4

if number_group == 0:
    print(f"The color is red")
if number_group == 1:
    print(f"The color is white")
if number_group == 2:
    print(f"The color is yellow")
if number_group == 3:
    print(f"The color is blue")
```

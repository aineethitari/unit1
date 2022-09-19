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

<img width="736" alt="Task1 1_Code" src="https://user-images.githubusercontent.com/112055062/191013556-604e9f1b-3ee3-4079-8518-c69bbad081ba.png">

**Task1.2** Using the program above, create another program that allows the user to enter a number and the program outputs the color that should be used in the locker.

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

<img width="1195" alt="Task1 2_Code" src="https://user-images.githubusercontent.com/112055062/191013757-da900656-5bed-4771-824f-0ad64123d357.png">

**Task1.3 [HL]** Create a program that receives a color from the user, validates the input,  and outputs the numbers of the lockers of the color provided. Use at least 10 different functions for Manipulating Strings (Learning Log Item 19)

```.py
msg="Please choose a color in lower case: red, white, yellow, or blue"

color = str(input(msg.swapcase()))
if not color:
    color = input(msg)

while color not in ["red","blue","yellow","white"]:
    color = input(f"{msg.center(80,'#')}").lower()

count = 0
while count <600:
    count += 1
    if color == "red":
        print(int(4 * count) - 3)
    if color == "white":
        print(int(4 * count) - 2)
    if color == "yellow":
        print(int(4 * count) - 1)
    if color == "blue":
        print(int(4 * count))        
```

<img width="1203" alt="Task1 3_Locker_Code" src="https://user-images.githubusercontent.com/112055062/191013252-fe476374-74e3-4e9e-98e6-f6b576125840.png">

**Task1.4 [HL]** Given a list of names of students in the format lastname, firstname, create a program that assigns an email address and a locker to each student and saves the results in a file in the format lastname, firstname, email, locker 

```.py
with open('students.csv') as file:
    all_stu = file.readlines()
    new_all_stu = []
    for stu_index in range(len(all_stu)):
        names = all_stu[stu_index].strip() #strip to remove \n
        split_name = names.split(",")
        f_name = split_name[0]
        l_name = split_name[1]
        grad_year = split_name[2]
        email = f"{grad_year}.{f_name}.{l_name}@uwcisak.jp"
        locker = f"{stu_index+1}"
        out_str = f"{f_name},{l_name},{email},{locker}\n"
        new_all_stu.append(out_str)

print(new_all_stu)

with open('new_students.csv','w') as file:
    file.writelines(new_all_stu)
```

<img width="1177" alt="Task1 4_Locker_Code" src="https://user-images.githubusercontent.com/112055062/191013215-e3084adb-cb62-40c9-ae60-e9bb8b5971d9.png">



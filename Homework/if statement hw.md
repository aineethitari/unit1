# If statement homework
## Write a program to sort alphabetically three names entered by the user. Note: Assume that only the first letter of names are the same. 

```.py
name_1 = input("Please enter the first name")
name_2 = input("Please enter the second name")
name_3 = input("Please enter the third name")

if name_1 < name_2:
    if name_2 < name_3:
        print(name_1, name_2, name_3)
    if name_2 > name_3:
        print(name_1, name_3, name_2)
if name_2 < name_1:
    if name_1 < name_3:
        print(name_2, name_1, name_3)
    if name_1 > name_3:
        print(name_2, name_3, name_1)
if name_3 < name_1:
    if name_1 < name_2:
        print(name_3, name_1, name_2)
    if name_1 > name_2:
        print(name_3, name_2, name_1)
exit()
```

## 　Create a program that calculates the median for a series of scores entered by the user. The user enters either 4 or 5 scores.

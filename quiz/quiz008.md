# Quiz008
```.py
room = int(input("Please enter room number "))
floor = (room//10) + 1
num = room%10
if floor == 11:
    floor = 10
if num == 0:
    num = 10
if num < 10:
    output = f"{floor}F0{num}"
if num == 10:
    output = f"{floor}F{num}"
print(output)
```

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

![Quiz008_flowchart](https://user-images.githubusercontent.com/112055062/191011742-cd0737c8-531a-4e00-b4bb-c5d5decc7603.png)

<img width="760" alt="Quiz008_code" src="https://user-images.githubusercontent.com/112055062/191011953-d4e67d1e-88f6-4279-b147-e5a2e8a0b245.png">

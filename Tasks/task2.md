# Task 2
```.py
from my_library import validate_int_input
color = ["\33[0;30m", "\33[0;31m", "\33[0;32m", "\33[0;34m"]
end_code = "\033[00m"

intro_msg = f"{color[2]} Welcome to EV Calculator{end_code}"
print(intro_msg.center(50,"-"))

menu = """1. Average time per kWh
2. Total kWh used
3. Total charge time
4. Show all data
"""
print("Options".center(50))
print(menu)

option = validate_int_input("Please enter an option [1-4]:")
while option>4 or option<1:
    option = validate_int_input(f"{option} is incorrect. Please enter an option[1-4]:")

with open("charging_log.csv","r") as file: #file is a variable #r=read
    ev_data = file.readlines()

if option == 4:
    i = 0
    for line in ev_data:
        if i>0:
            print(f"{color[2]}Log No.{i} {line.strip()}{end_code}") #strip is used to remove the extra space between each lines
        i += 1
if option == 2:
    i = 0
    total_energy = 0.0
    for line in ev_data:
        if i>0: #this keeps the first line which is the title
            values = line.split(',')
            charge = values[1]
            charge_cleaned = charge [:5]
            charge_float = float(charge_cleaned)
            total_energy += charge_float
        i += 1

    print(f"{color[1]}Total energy used so far {total_energy} kWh {end_code}")

if option == 3:
    i = 0
    total_time = 0
    for line in ev_data:
        if i>0:
            values = line.split(',')
            date = values[0]
            charge = values[1]
            duration = values[2].split(':')
            total_time += (int(duration[0])*3600 + int(duration[1])*60 + int(duration[2]))
        i += 1
    hour = total_time//3600
    min = total_time % 3600//60
    sec = total_time % 60
    print(f"{color[2]}The total charge time is {hour} hours, {min} minutes, and {sec} seconds {end_code}")
    print(total_time)

if option == 1:
    i = 0
    total_energy = 0
    total_time = 0
    for line in ev_data:
        if i>0:
            values = line.split(',')
            date = values[0]
            charge = values[1]
            duration = values[2].split(':')
            total_time += (int(duration[0])*3600 + int(duration[1])*60 + int(duration[2]))
            total_energy += float(charge[0:5])
            avg_time = int(total_time/total_energy)
        i += 1
    print(f"{color[2]} The average time per energy is {avg_time} seconds/kwh.{end_code}")

    # avg_time_per_kwh = total_time/total_energy
    # print(avg_time_per_kwh)


print("Bye Bye")
```

Images of the results:

<img width="477" alt="Task 2 " src="https://user-images.githubusercontent.com/112055062/194765056-58f30543-356d-4d7c-a8ef-1ce7134456f5.png">

<img width="367" alt="Task 2 option 2" src="https://user-images.githubusercontent.com/112055062/194765064-3d2be4fd-4e81-4a04-a69c-8d9eb43b0452.png">

<img width="546" alt="Task 2 option 3" src="https://user-images.githubusercontent.com/112055062/194765071-dd7b4d44-254e-47f5-a237-1e83e8019c48.png">

<img width="405" alt="Task 2 option 4" src="https://user-images.githubusercontent.com/112055062/194765078-aeb145a1-838b-454f-9a98-d5dd682bc49f.png">

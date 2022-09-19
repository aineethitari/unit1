# Quiz 007
## Create a program that create 10 random password with digits and letters of length 20.
[HL] Ask the user for the length and if symbols should be included. Print answer in RED
```.py
import random
end_code = "\033[00m"
red = "\33[0;31m"

length = input("How many characters do you need in your password? ")
while not length.isdigit():
    length = input(f"{red} Error, please enter a number{end_code}")
length = int(length)


symbol = str(input("Would you like to include symbol? Please answer yes or no"))
while not symbol in ["yes", "no"]:
    symbol = str(input(f"{red}Error, please enter yes or no{end_code}"))

for m in range(10):
    password = ""
    for n in range(length):
        rand_num = random.randint(48,122)

        # if not symbols
        if symbol == "no":
            while 65>rand_num>57 or 97>rand_num>90:
                rand_num = random.randint(48,122)
        # if symbols


        rand_letter = chr(rand_num)
        password = password + rand_letter

    print(f"Your password {m+1} is{red} {password} {end_code}")
    ```
    
![Quiz007 Flowchart](https://user-images.githubusercontent.com/112055062/190997897-0bc51d7f-3ea0-4684-ad0f-9180e7fed492.jpg)



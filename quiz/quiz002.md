#Quiz002
```.py
#Given 2 numbers, A and B, Output TRUE if one of them is 20 or if their sum is 20.
'''
This is a multiline comment
'''
number_A = int(input("Please enter a number "))
number_B = int(input("Please enter a number "))
#print message to user to confirm inputs are correct
print(f"You entered {number_A} and {number_B}")

output = False
if number_A == 20 or number_B == 20:
  output = True

if number_A + number_B == 20:
  output = True

print(f"The answer to the quiz 002 is {output}")
```

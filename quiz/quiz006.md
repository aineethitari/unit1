# Quiz 006
## Given a string, create a program that produces the sum of the characters in the string.
```.py
text = str(input("Please enter a message "))

text = text.lower()

count = 0
value = 0
while count < len(text):
    print(count,text[count], ord(text[count]) )
    value = value + ord(text[count]) - 96
    count = count + 1

print(value)

value = 0
for number in range(len(text)):
    value = value + ord(text[number]) - 96

print(f"this is the second result{value}")
```

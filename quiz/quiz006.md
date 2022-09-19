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

![quiz006 flowchart drawio](https://user-images.githubusercontent.com/112055062/190990098-031bfdf2-c781-46a0-82d5-ce392daab892.png)

<img width="824" alt="Quiz006_Results" src="https://user-images.githubusercontent.com/112055062/190990557-393ead7a-30ba-44cc-a8ac-cfe8092ac95b.png">

# Quiz 005 
## Given a number, create a program that produces the output factors. 
## [HL]  Check if the number is a Perfect Number and show True or False

```.py
number = int(input("Please enter a number"))
counter = 1
sum = 0
while counter < number:
    if number % counter == 0:
        sum = sum + counter
        print(counter)
    counter += 1
if number ==sum:
    print("True")
else:
    print("False")
```

![Quiz005 flowchart edit](https://user-images.githubusercontent.com/112055062/189649863-43557a65-48b4-4f6e-8a35-f3b02853852b.jpeg)

**Fig.1** Flowchart of Quiz005

<img width="461" alt="Quiz005_Results" src="https://user-images.githubusercontent.com/112055062/190999538-7633841c-19e3-41db-a20d-76e84caf57dd.png">

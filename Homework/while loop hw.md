# While Loop Homework from Slides
## Create a program for the Game “Guessing a number between 0 and 100” the computer is the player that knows the secret number. The user tries to guess the number by entering guesses, the computer indicates if the number is higher or lower than the secret number.  

```.py
# Create a program for the Game “Guessing a number between 0 and 100” the computer is the player that knows the secret number. The user tries to guess the number by entering guesses, the computer indicates if the number is higher or lower than the secret number.  

import random
number = random.randint(1, 100)
guess = int(input("Guess a number from 1 to 100 "))
guess = int(guess)

while guess != number:
    if guess < number:
        guess = int(input("Incorrect number. Please enter a higher number."))
    if guess > number:
        guess = int(input("Incorrect number. Please enter a lower number."))
    else:
        print(f"Congratulations! You guessed the number {number} correctly!")

exit()
```

<img width="1341" alt="Guess number between 1-100" src="https://user-images.githubusercontent.com/112055062/189517266-b63b99a5-d35b-4551-8158-6d5235093a4c.png">

**Fig.1** Image from Pycharm


# Quiz 009 

<img width="380" alt="Quiz 009" src="https://user-images.githubusercontent.com/112055062/194736190-9487127b-67b5-4f9f-b8fe-fde777e63f85.png">

```.py
def ciphered_shift(msg:str,shift:int)->str:
    new_msg = ""
    for character in msg:
        if ord(character) >= 91 and ord(character) <= 96: #for spaces and symbols
            new_number = ord(character)
        if ord(character) >= 32 and ord(character) <= 64: #for spaces and symbols
            new_number = ord(character)
        if ord(character) >= 123:
            new_number = ord(character)

        if ord(character) >= 97 and ord(character) <= 122:
            new_number = ord(character) + shift
            if new_number > 122:
                new_number = ord(character) + shift - 26
            if new_number < 97:
                new_number = ord(character) + shift + 26

        if ord(character) >= 65 and ord(character)<=90:
            new_number = ord(character) + shift
            if new_number > 90:
                new_number = ord(character) + shift - 26
            if new_number < 65:
                new_number = ord(character) + shift + 26

        new_msg += chr(new_number)


    return new_msg

#----------------
msg = input("please enter a message")
shift = int(input("please enter shift"))

print(ciphered_shift(msg,shift))
```

Image of the result:

<img width="1097" alt="quiz 009 result" src="https://user-images.githubusercontent.com/112055062/194736265-0781341c-5264-439c-8c97-a70a89e57431.png">


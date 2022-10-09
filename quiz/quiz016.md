#Quiz 016

<img width="548" alt="quiz 016" src="https://user-images.githubusercontent.com/112055062/194755260-29edac4f-c7aa-43d1-8c46-6f275da65cce.png">

```.py
def blackBoxThree(given:str)->str:
    output = ""
    count = []
    for letter in given.lower():
        if letter.isalpha():
            included = -1
            index = 0
            for item in count:
                if letter in item:
                    included = index
                index += 1

            if included == -1:
                count.append([letter,1])
            else:
                count[included][1] += 1
            output += str(count[included][1])
        else:
            output += letter
    return output

input = input("enter message")
test1 = blackBoxThree(input)
print(test1)
```

![Quiz016 (1)](https://user-images.githubusercontent.com/112055062/194758225-efb4c10a-2596-4ed0-80e5-b0e8bc66a9e0.jpg)

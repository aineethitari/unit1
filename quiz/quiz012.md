# Create a function that recieves integer 2<N<10, and returns the multiplication table for the number up to 9

```.py
def mulTable(x:int)->str:

    out = ""
    for i in range(0,8):
        out += f"{x}x{i+1}={x*(i+1)}\n" #+ is concatenation = putting two strings together
    return out

test1 = mulTable(int(input("Please insert an integer ")))
print(test1)
```

Image of the result:

<img width="867" alt="quiz012" src="https://user-images.githubusercontent.com/112055062/192402881-cf75341d-1a7f-4d8a-a2cc-dc55ec6d4a5d.png">

Image of the flow diagram:

![Quiz012_Flowchart](https://user-images.githubusercontent.com/112055062/193770080-fdd13077-1574-4d47-b5b9-16fe4770c098.jpg)

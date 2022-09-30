# quiz 013
## Create a function that receives one input and produces the output shown.

```.py
def numbers(a:int,b:int)->int:
    difference = abs(a-b)
    if a == b:
        difference = a
    output = (a * b) - difference
    return output

print(numbers(10,10))
```

Result

<img width="498" alt="Quiz013 result" src="https://user-images.githubusercontent.com/112055062/193206533-89f7a8a5-7981-4d90-91b0-c0acb87e03db.png">


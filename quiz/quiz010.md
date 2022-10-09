# Quiz 010

<img width="563" alt="Quiz 10 " src="https://user-images.githubusercontent.com/112055062/194737545-1bc611b2-2b93-4533-b4da-546002aac60c.png">

```.py
def powersTen(x:str)->str:
    '''
    This function produces the power of ten for the number provided
    :param x: number: integer
    :return: string
    '''


    x_list = x.split()
    num = x_list[0]
    print(x_list)
    print(num)
    num = int(num)


    out = (f"""
    {num * (10**12)}          Tera
    {num * (10**9)}           Giga
    {num * (10**6)}           Mega
    {num * (10**3)}           kilo
    {num * (10**0)}           unit
    {num * (10**-3)}          mili
    {num * (10**-6)}          micro
    {num * (10**-9)}          nano
    {num * (10**-12)}         pico
    """)

    return out

#-----------------------------
input = input("Please enter string with units")
test1 = powersTen(x=input)
print(test1)
```

Image of the result

<img width="621" alt="quiz 010 result" src="https://user-images.githubusercontent.com/112055062/194738638-a764057a-b4fd-45af-be80-ab5185b5abf4.png">



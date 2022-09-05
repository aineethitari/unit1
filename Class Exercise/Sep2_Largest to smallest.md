# Sep 2 2022 class exercise
## Create a program that organizes from largest to smallest three heights in cms entered by the user
```.py
A = int(input("Please enter height in cm "))
B = int(input("Please enter height in cm "))
C = int(input("Please enter height in cm "))
if A > B:
    if B > C:
        Output = A, B, C
    elif A > C:
        Output = A, C, B
    else:
        Output = C, A, B
elif C > B:
    Output = C, B, A
    if C > A:
        Output = B, C, A
    else:
        Output = B, A, C

print(f"The largest to smallest heights are {Output}.")
```
## Flow Chart:

![largest to smallest](https://user-images.githubusercontent.com/112055062/188367076-2a71f92d-9dcf-402c-bfd6-6fc77ff8819a.JPG)

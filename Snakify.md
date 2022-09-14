# Chapter 1 - Input, print and numbers

## Sum of three numbers

Write a program that takes three numbers and prints their sum. Every number is given on a separate line.

```.py
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```

Image of the results

<img width="802" alt="Test run 1" src="https://user-images.githubusercontent.com/112055062/187020010-2e873d7e-b089-4572-8d3c-08d747c546bb.png">

## Hi John

Write a program that greets the person by printing the word "Hi" and the name of the person. See the examples below.

```.py
print('Hi',input())
```
Image of the results

<img width="625" alt="Hi John" src="https://user-images.githubusercontent.com/112055062/187020110-c60604b7-c3c5-4c9e-a78c-d1899e7495e0.png">

## Square

Write a program that takes a number and print its square.

```.py
a=int(input())
print(a**2)
```
Image of the results

<img width="650" alt="Square1" src="https://user-images.githubusercontent.com/112055062/187020325-b2bd0099-4316-4b60-ae73-f7688d060e48.png">
<img width="631" alt="Square2" src="https://user-images.githubusercontent.com/112055062/187020326-3f46f00f-6642-4295-8d41-fa6f6993bece.png">

## Area of right-angled triangle

Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line.

```.py
b = int(input())
h=int(input())
# Print the result with print()
print((b*h)/2)
```

Image of the results

<img width="608" alt="right angle triangle" src="https://user-images.githubusercontent.com/112055062/187020510-890d8f2f-b281-42aa-b4cf-08e31fc6dd39.png">

## Hello, Harry!

Write a program that greets the user by printing the word "Hello", a comma, the name of the user and an exclamation mark after it. See the examples below.

```.py
print('Hello'+','+' '+name+'!')
```

Image of the results

<img width="839" alt="Hello Harry" src="https://user-images.githubusercontent.com/112055062/187020650-59953b4d-ce4a-4bde-9b56-9cb964b30e28.png">

## Apple sharing

N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
The program reads the numbers N and K. It should print the two answers for the questions above.

```.py
N = int(input())
K = int(input())
# Print the result with print()
print(K//N)
print(K%N)
```

Image of the results

<img width="821" alt="Apple sharing" src="https://user-images.githubusercontent.com/112055062/187020909-9d4f7a53-1174-4fbb-a2e4-ef009805a2da.png">

## Previous and next

Write a program that reads an integer number and prints its previous and next numbers. See the examples below for the exact format your answers should take. There shouldn't be a space before the period.

```.py
a = int(input())
b = int(a+1)
c = int(a-1)
print('The next number for the number '+ str(a) + ' is ' + str(b) + '.')
print('The previous number for the number ' + str(a) + ' is ' + str(c) + '.')
```

Image of the results

<img width="1059" alt="Previous Next" src="https://user-images.githubusercontent.com/112055062/187021132-5f0bf206-e1d5-4f7b-bc37-5843c472edfc.png">

## Two timestamps

A timestamp is three numbers: a number of hours, minutes and seconds. Given two timestamps, calculate how many seconds is between them. The moment of the first timestamp occurred before the moment of the second timestamp.

```.py
h1 = int(input())*3600
m1 = int(input())*60
s1 = int(input())
a = int(h1+m1+s1)
h2 = int(input())*3600
m2 = int(input())*60
s2 = int(input())
b = int(h2+m2+s2)
print(b-a)
```

Image of the results

<img width="863" alt="Two timestamps" src="https://user-images.githubusercontent.com/112055062/187021419-96c55865-8607-48a6-95ef-c588f4d5ed20.png">

<img width="873" alt="Two timestamps2" src="https://user-images.githubusercontent.com/112055062/187021425-0363158e-e393-4f29-9d8f-c15876373222.png">

## School desks

A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.

In the first test there are three groups. The first group has 20 students and thus needs 10 desks. The second group has 21 students, so they can get by with no fewer than 11 desks. 11 desks is also enough for the third group of 22 students. So we need 32 desks in total.

```.py
a = int(input())
b = int(input())
c = int(input())
print((a//2) + (a%2) + (b//2) + (b%2) + (c//2) + (c%2))
```

Image of the results

<img width="859" alt="School Desks" src="https://user-images.githubusercontent.com/112055062/187021598-ab30a01b-6695-45f5-abfe-674791ee633b.png">

# Chapter 2 - Integer and float numbers

## Last digit of integer

Given an integer number, print its last digit.

```.py
a = int(input())
print(a % 10)
```

Image of the results

<img width="850" alt="Last digit of integer1" src="https://user-images.githubusercontent.com/112055062/187022098-2738dc63-ce6e-4f16-8041-581a6909f64f.png">

<img width="857" alt="Last digit of integer2" src="https://user-images.githubusercontent.com/112055062/187022102-5c6f6730-7a7a-4316-8c47-e81cdf96eb7e.png">

<img width="854" alt="Last digit of integer3" src="https://user-images.githubusercontent.com/112055062/187022110-9a102be9-96d9-44fb-b74b-790fefb6a30b.png">

## Two digits

Given a two-digit number, print its digits separately.

```.py
a=int(input())
print(a//10 , a%10)
```

Image of the results

<img width="373" alt="Two digits" src="https://user-images.githubusercontent.com/112055062/187928801-d8435e42-7c58-4096-b51b-6129cff0958a.png">

## Swap digits

Given a two-digit number, swap its digits as shown in the tests below

```.py
a=int(input())
b=a%10
c=a//10
print(b*10 + c)
```

Image of the results

<img width="369" alt="Swap digit" src="https://user-images.githubusercontent.com/112055062/187933571-3c64b22c-c695-4bf4-b4d0-c0cc93f2d176.png">

## Last two digits

Given an integer number, print its last two digits

```.py
a=int(input())
units=a%10
tenths=a%100 - a%10
print(units + tenths)
```

Image of the results

<img width="378" alt="Last two digits" src="https://user-images.githubusercontent.com/112055062/187935850-c19edeb3-32ed-47cc-9960-280bc959f8b5.png">

## Tens digit

Given an integer. Print its tens digit.

```.py
a= int(input())
print(a//10 %10)
```

Image of the results

<img width="845" alt="Tens digit1" src="https://user-images.githubusercontent.com/112055062/187022291-70f21030-0de0-412b-8de6-566251a638e0.png">

## Sum of digits

Given a three-digit number. Find the sum of its digits.

```.py
n=int(input())
print(n%10 + n//10%10 + n//100%10)
```

Image of the results

<img width="818" alt="Sum of digits" src="https://user-images.githubusercontent.com/112055062/187025476-929c36a3-48fc-4e80-8d6e-b7de0c47f969.png">

## Reverse three digits

Given a three-digit integer number, print its digits in a reversed order

```.py
a = int(input())
units = a%10
tenths = a//10 %10
hundredths = a//100 
print(int(units*100+tenths*10+hundredths))
```

<img width="388" alt="Reverse three digits" src="https://user-images.githubusercontent.com/112055062/187950576-323c0b5a-fec1-4495-b076-cb4f7f5a19bf.png">

## Merge two numbers

Given two two-digit numbers, merge their digits as shown in the tests below.

```.py
number_1 = int(input())
number_2 = int(input())

thousands = (number_1//10)*1000
hundreds = (number_2//10)*100
tens = (number_1%10)*10
ones = (number_2%10)

print(thousands + hundreds + tens + ones)
```

Image of the results

<img width="370" alt="merge two numbers" src="https://user-images.githubusercontent.com/112055062/188882618-c4824fe3-461a-4536-8ee6-040f4211829e.png">

## Cyclic rotation

Given a four-digit integer number, perform its cyclic rotation by two digits, as shown in the tests below.

```.py
a = int(input())

print(a % 100 * 100 + a // 100)
```

Image of the results

<img width="383" alt="Cyclic rotation" src="https://user-images.githubusercontent.com/112055062/188886070-fa7bf261-dc31-4f67-b0ee-507a6dc844d8.png">

## Fractional part

Given a positive real number, print its fractional part.

```.py
n=float(input())
print(n-int(n))
```

Image of the results

<img width="812" alt="Fractional part" src="https://user-images.githubusercontent.com/112055062/187025799-6d7eba84-2a35-4caa-855e-ea9b02890f5d.png">

## First digit after decimal point

Given a positive real number, print its first digit to the right of the decimal point.

```.py
a=float(input())
b = a//1
c = a-b
print(c*10//1)
```

Image of the results

<img width="832" alt="First digit after decimal point" src="https://user-images.githubusercontent.com/112055062/187026030-9393e4e7-370a-44bb-900d-f45c153aefb9.png">

## Car route

A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.

```.py
N = int(input())
M = int(input())
import math
print(math.ceil(M/N))
```

Image of the results

<img width="806" alt="Car route1" src="https://user-images.githubusercontent.com/112055062/187026316-574b6742-aff6-45ed-9ef7-d157c72f5530.png">

<img width="812" alt="Car route2" src="https://user-images.githubusercontent.com/112055062/187026323-13282892-d0e6-41db-a5eb-ea8d2f58b095.png">

## Day of week

Let's count the days of the week as follows: 0 - Sunday, 1 - Monday, 2 - Tuesday, ..., 6 - Saturday. Given an integer K in the range 1 to 365, find the number of the day of the week for the K-th day of the year provided that this year's January 1 is Thursday.

```.py
number = int(input())
number_group = (number+3)%7

if number_group == 0:
    print("0")
if number_group == 1:
    print("1")
if number_group == 2:
    print("2")
if number_group == 3:
    print("3")
if number_group == 4:
    print("4")
if number_group == 5:
    print("5")
if number_group == 6:
    print("6")
```

Image of the results 

<img width="379" alt="day of week " src="https://user-images.githubusercontent.com/112055062/190135655-f7d0d641-1b4d-4595-b968-c381f4f5b112.png">

## Digital clock

Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).

For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am. So the program should print 2 30.

```.py
a = int(input())
print(a//60)
print(a%60)
```

Image of the results

<img width="835" alt="Digital clock" src="https://user-images.githubusercontent.com/112055062/187026591-8e7d3b21-66ae-4e93-9cb0-d86c92f3033d.png">

## Total cost

A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes. A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

```.py
A = int(input())
B = int(input())
N = int(input())

print(A*N + B*N//100)
print(B*N % 100)
```


Image of the results

<img width="813" alt="Total cost" src="https://user-images.githubusercontent.com/112055062/187027151-289cc49f-ea7f-4712-aa6e-9433474a6695.png">

<img width="805" alt="Total cost2" src="https://user-images.githubusercontent.com/112055062/187027162-5431a545-c958-4646-a923-753784b26d5a.png">

## Century

Given a year as a positive integer, print its century. Mind that the 20th century began on 1901 and ended on 2000.

```.py
year = int(input())
century = year//100 +1
if year%100 == 0:
    century = year//100
print(century)
```

Image of the results

<img width="617" alt="Century" src="https://user-images.githubusercontent.com/112055062/190162688-a7382adb-99dd-42a0-a35f-46202e3abe02.png">

## Snail

A snail goes up A feet during the day and falls B feet at night. How long does it take him to go up H feet?
Given three integer numbers H, A and B (A > B), the program should output a number of days.

```.py
H = int(input())
A = int(input())
B = int(input())

from math import ceil
D = ceil((H - A) / (A - B)) + 1
print(D)
```

Image of the results

<img width="620" alt="Snail" src="https://user-images.githubusercontent.com/112055062/190174951-5427ec13-9e19-44fa-9194-6223aa2e2b7a.png">

## Clock face-1

H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). Determine the angle (in degrees) of the hour hand on the clock face right now.

```.py
h = int(input())
m = int(input())
s = int(input())
print( (h*3600 + m*60 + s) * (1/120))
```

Image of the results

<img width="806" alt="Clock face 1" src="https://user-images.githubusercontent.com/112055062/187027337-828f7a6c-85de-43dc-a524-400e269dff79.png">

<img width="811" alt="Clockface1 2" src="https://user-images.githubusercontent.com/112055062/187027343-7851d0cc-9a8e-460f-9871-891015c52e84.png">

## Clock face -2

Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers.

```.py
a = float(input())
print( (a*2) %60 *6)
```

Image of the results

<img width="615" alt="Clockface 2" src="https://user-images.githubusercontent.com/112055062/187027505-99680396-dc78-46d2-9e53-445c87558cc8.png">

# Chapter 3 - Conditions: if, then, else

## Is positive

Given an integer, print "YES" if it's positive and print "NO" otherwise.

```.py
number = int(input())
if number > 0:
    print("YES")
else:
    print("NO")
```

Image of the results

<img width="620" alt="Snail" src="https://user-images.githubusercontent.com/112055062/190180554-5f5343be-daee-4ed6-bf0a-7bcdf43559bf.png">

## Minimum of two numbers

Given two integers, print the smaller value.

```.py
a=int(input())
b=int(input())
if a>b:
    print (b)
else: 
    print(a)
```

Image of the results

<img width="847" alt="minimum of two numbers" src="https://user-images.githubusercontent.com/112055062/187186733-256fcab2-949b-491b-9c58-6a0c6b449835.png">

## Sign function

For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
Try to use the cascade if-elif-else for it.

```.py
x = int(input())
if x > 0:
    print(1)
elif x==0:
    print(0)
if x<0:
    print(-1)
```

Image of the results

<img width="828" alt="Sign function" src="https://user-images.githubusercontent.com/112055062/187323778-6bfcb8fd-7847-4612-bd64-28dd99f7ead1.png">

## Minimum of three numbers

Given three integers, print the smallest value.

```.py
a = int(input())
b = int(input())
c = int(input())
if a < b and a < c :
    print(a)
elif b<c and b<c:
    print(b)
else:
    print(c)
```

Image of the results

<img width="828" alt="Sign function" src="https://user-images.githubusercontent.com/112055062/187324322-2b32fa10-b6a0-4517-90b5-3f19be150cbd.png">

## Equal numbers

Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).

```.py
a = int(input())
b = int(input())
c = int(input())
if a==b and b==c:
    print(3)
elif a==b and b!=c :
    print(2)
elif b==c and c!=a:
    print(2)
elif c==a and a!=b:
    print(2)
else :
    print(0)
```

Image of the results

<img width="823" alt="Equal numbers" src="https://user-images.githubusercontent.com/112055062/187332230-82525f7a-b0f9-442c-8bcb-393c93f5cad6.png">


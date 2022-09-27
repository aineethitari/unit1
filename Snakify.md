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

## Is odd

Given an integer, print "YES" if it's odd and print "NO" otherwise.

```.py
number = int(input())
if number % 2 == 0:
    print("NO")
else:
    print("YES")
```

Image of the results

<img width="247" alt="Is odd" src="https://user-images.githubusercontent.com/112055062/190182292-3b952336-5d84-443a-b4ec-576dc0d119f6.png">

## Is even

Given an integer, print "YES" if it's even and print "NO" otherwise.

```.py
num = int(input())
if num%2 == 0:
    print("YES")
else:
    print("NO")
```


Image of the results

<img width="247" alt="Is odd" src="https://user-images.githubusercontent.com/112055062/190183454-4b729ece-e2e8-4212-8ed2-18d785c1a8cb.png">

## Ends on seven

Given an integer, print "YES" if it's last digit is 7 and print "NO" otherwise.

```.py
num = int(input())
last_digit = num%10
if last_digit%7 == 0:
    print("YES")
else:
    print("NO")
```

Image of the results

<img width="436" alt="Ends on seven" src="https://user-images.githubusercontent.com/112055062/190185174-229bcfb9-2f81-4bdf-850b-bbec2cdc3c48.png">

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

## Are both odd

Given two integers, print "YES" if they're both odd and print "NO" otherwise.

```.py
a = int(input())
b = int(input())
if a%2!=0 and b%2!=0:
    print("YES")
else:
    print("NO")
```

Image of the results

<img width="276" alt="Are both odd" src="https://user-images.githubusercontent.com/112055062/190187077-00ffe6b5-0134-436f-800e-eeb25f6136b3.png">

## At least one odd

Given two integers, print "YES" if at least one of them is odd and print "NO" otherwise.

```.py
a = int(input())
b = int(input())
if a%2!=0 or b%2!=0:
    print("YES")
else:
    print("NO")
```

Image of the results

<img width="321" alt="At least one odd" src="https://user-images.githubusercontent.com/112055062/190188430-1aa15e60-6c45-45fc-9a39-812fc9440c9a.png">

## Exactly one odd

Given two integers, print "YES" if exactly one of them is odd and print "NO" otherwise.

```.py
a = int(input())
b = int(input())
if a%2 != 0 and b%2 == 0:
        print("YES")
elif a%2 == 0 and b%2 != 0:
        print("YES")
else:
    print("NO")
```

Image of the results:

<img width="321" alt="At least one odd" src="https://user-images.githubusercontent.com/112055062/190191431-8f87e3a2-ba0f-47ff-bdfe-195a8aa0a2df.png">

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

## Numbers in ascending order

Given three different integers, print YES if they're given in ascending order, print NO otherwise.

```.py
a = int(input())
b = int(input())
c = int(input())
if a<b<c:
    print("YES")
else:
    print("NO")
```

<img width="281" alt="ascending order" src="https://user-images.githubusercontent.com/112055062/190194112-495f1a16-2772-4852-a5a6-17b2a4d43201.png">

## Is three digit

Given an integer, print "YES" if it's a three-digit number and print "NO" otherwise.

```.py
a = int(input())
if 1000>a>99:
    print("YES")
else:
    print("NO")
```

Image of the results

<img width="445" alt="Is three digit" src="https://user-images.githubusercontent.com/112055062/190195373-0180184c-5eec-4262-a5dc-e86b1d2a3f82.png">

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

## Rook move

Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.

```.py
columnA = int(input())
rowA = int(input())
columnB = int(input())
rowB = int(input())

if columnA == columnB:
    outcome = "YES"
elif rowA == rowB:
    outcome = "YES"
else:
    outcome = "NO"
print(outcome)
```

Image of the results

<img width="633" alt="rook move" src="https://user-images.githubusercontent.com/112055062/191705369-cc445469-4226-4d5b-9d33-a8a36aba6745.png">

## Chess board - black square

Given a square of a chessboard. Print BLACK if it's black and print WHITE otherwise

```.py
column = int(input())
row = int(input())
if column in [1,3,5,7]:
    if row in [1,3,5,7]:
        outcome = "BLACK"
    if row in [2,4,6,8]:
        outcome = "WHITE"
if column in [2,4,6,8]:
    if row in [1,3,5,7]:
        outcome = "WHITE"
    if row in [2,4,6,8]:
        outcome = "BLACK"
print(outcome)
```

Image of the result

<img width="511" alt="Chess board-black square" src="https://user-images.githubusercontent.com/112055062/191762949-f2cf78d2-ba5b-41cd-bcf8-06adaad9f824.png">

## Chess board - same color

Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

```.py
columnA= int(input())
rowA = int(input())
columnB = int(input())
rowB = int(input())

if columnA%2==0 and rowA%2==0:
    outcomeA = "black"
if columnA%2!=0 and rowA%2!=0:
    outcomeA = "black"
if columnA%2==0 and rowA%2!=0:
    outcomeA = "white"
if columnA%2!=0 and rowA%2==0:
    outcomeA = "white"

if columnB%2==0 and rowB%2==0:
    outcomeB = "black"
if columnB%2!=0 and rowB%2!=0:
    outcomeB = "black"
if columnB%2==0 and rowB%2!=0:
    outcomeB = "white"
if columnB%2!=0 and rowB%2==0:
    outcomeB = "white"

if outcomeA == outcomeB:
    print("YES")
if not outcomeA == outcomeB:
    print("NO")
```

Image of the result

<img width="351" alt="chess board - same color" src="https://user-images.githubusercontent.com/112055062/191777837-cd2bc2d1-7496-4608-8225-ebc3f10316b3.png">

## Distance to closest point

Given the coordinates of the three points A, B, and C on a line. Print a distance from the point A to closest point to it.

```.py
A = int(input())
B = int(input())
C = int(input())
A_to_B = abs(A-B)
A_to_C = abs(A-C)
if A_to_B < A_to_C:
    print(A_to_B)
if A_to_C < A_to_B:
    print(A_to_C)
```

Image of the result

<img width="344" alt="Distance to closest point" src="https://user-images.githubusercontent.com/112055062/191779371-bc25bc97-d24a-4455-8916-a3e27481ab11.png">

## Digits in ascending order

Given a three-digit integer, print YES if its digits go in ascending order, print NO otherwise.

```.py
number = int(input())
number = str(number)
if number[0] < number[1] < number[2]:
    print("YES")
else:
    print("NO")
```

Image of the result

<img width="525" alt="digits in ascending order" src="https://user-images.githubusercontent.com/112055062/191780384-25f0995f-77b2-4a1b-850a-a2d8b4d29074.png">

## Four-digit palindrome

A palindrome is a number which reads the same when read forward as it it does when read backward. Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.

```.py
number = str(input())
if number[0] == number[3] and number[1] == number[2]:
    print("YES")
else:
    print("NO")
```

Image of the result

<img width="486" alt="Four digit palindrome" src="https://user-images.githubusercontent.com/112055062/191781484-e017e4da-742f-4e16-8e74-e5dd26695d04.png">

## King move

Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.

```.py
columnA = int(input())
rowA = int(input())
columnB = int(input())

rowB = int(input())
if columnB == columnA + 1:
    columnB = "check"
if columnB == columnA - 1:
    columnB = "check"
if columnB == columnA:
    columnB = "check"
if rowB == rowA + 1:
    rowB = "check"
if rowB == rowA - 1:
    rowB = "check"
if rowB == rowA:
    rowB = "check"

if columnB == "check" and rowB == "check":
    print("YES")
else:
    print("NO")
```

Image of the result

<img width="645" alt="King move" src="https://user-images.githubusercontent.com/112055062/192127027-7d195553-bb7a-45a4-90ed-9e65ef52a58b.png">

## Bishop moves

In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.
The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.

```.py
columnA = int(input())
rowA = int(input())
columnB = int(input())
rowB = int(input())
if abs(columnA-columnB) == abs(rowA-rowB):
    print("YES")
else:
    print("NO")
```

Image of the result:

<img width="618" alt="Bishop move" src="https://user-images.githubusercontent.com/112055062/192140009-18894174-3430-49c9-9044-635d73c2ba1c.png">

## Queen move

Chess queen moves horizontally, vertically or diagonally to any number of cells. Given two different cells of the chessboard, determine whether a queen can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a queen can go from the first cell to the second in one move, or NO otherwise.

```.py
columnA = int(input())
rowA = int(input())
columnB = int(input())
rowB = int(input())
if (abs(columnA-columnB)) == (abs(rowB-rowA)) or columnA == columnB or rowA == rowB:
    output = "YES"
else:
    output = "NO"
print(output)
```

Image of the result

<img width="618" alt="Bishop move" src="https://user-images.githubusercontent.com/112055062/192140964-555a3cba-c928-4746-b78e-882dd2b20e6b.png">

## Index of outlier

Given three integers: two are equal to each other and the third one is different. Print the index number of this different one - 1, 2 or 3.

```.py
a = int(input())
b = int(input())
c = int(input())
if a == b:
    print("3")
if a == c:
    print("2")
if b == c:
    print("1")
```

Image of the result

<img width="296" alt="Index of outlier" src="https://user-images.githubusercontent.com/112055062/192141078-16332746-7c90-4c65-9c08-6d10d1549ed6.png">

## Knight move

Chess knight moves like the letter L. It can move two cells horizontally and one cell vertically, or two cells vertically and one cells horizontally. Given two different cells of the chessboard, determine whether a knight can go from the first cell to the second in one move.
The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a knight can go from the first cell to the second in one move, or NO otherwise.

```.py
columnA = int(input())
rowA = int(input())
columnB = int(input())
rowB = int(input())
if (columnA + 2 == columnB or columnA - 2 == columnB) and (rowA + 1 == rowB or rowA - 1 == rowB):
    output = "YES"
elif (rowA + 2 == rowB or rowA - 2 == rowB) and (columnA + 1 == columnB or columnA -1 == columnB):
    output = "YES"
else:
    output = "NO"
print(output)
```

Image of the result

<img width="483" alt="Knight move" src="https://user-images.githubusercontent.com/112055062/192146930-b131392b-95d9-4f34-a15f-d1c579d382ee.png">

## Chocolate bar

Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. Determine whether it is possible to split it so that one of the parts will have exactly k squares.
The program reads three integers: n, m, and k. It should print YES or NO.

```.py
n = int(input())
m = int(input())
k = int(input())
if n*m > k:
    if k % n == 0 or k % m == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
```

Image of the result:

<img width="475" alt="chocolate bar" src="https://user-images.githubusercontent.com/112055062/192147901-04f6ae3f-bfe8-40b9-9aa8-c348eee3d1cc.png">

## Leap year

Given the year number. You need to check if this year is a leap year. If it is, print LEAP, otherwise print COMMON.
The rules in Gregorian calendar are as follows:

a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
a year is always a leap year if its number is exactly divisible by 400
Warning. The words LEAP and COMMON should be printed all caps.

```.py
year = int(input())
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("LEAP")
else:
    print("COMMON")
```

Image of the result:

<img width="284" alt="Leap year" src="https://user-images.githubusercontent.com/112055062/192148136-917414dd-d663-40ee-8cc7-6b95b431d609.png">

## Days in month

Given a month - an integer from 1 (January) to 12 (December), print the number of days in it in the year 2017 (or any other non-leap year).

```.py
month = int(input())
if month in [4,6,9,11]:
    print("30")
elif month == 2:
    print("28")
else:
    print("31")
```

Image of the result:

<img width="401" alt="Days in month" src="https://user-images.githubusercontent.com/112055062/192148382-d198d680-dda2-4032-85b5-2f1dcb58ada9.png">

## Next day

Given the month (an integer from 1 to 12) and the day in it (an integer from 1 to 31) in the year 2017 (or in any other common year), print the month and the day of the next day to it. The first test corresponds to March 30 and March 31. The second test corresponds to March 31 and April 1.

```.py
month = int(input())
day = int(input())

if month == 12 and day == 31:
    month = 1
    day = 1
    
elif (month in [1,3,5,7,8,10,12] and day == 31) or (month in [4,6,9,11] and day == 30) or (month == 2 and day == 28):
    month += 1
    day = 1

else:
    day += 1

print(month)
print(day)
```

Image of the result:

<img width="611" alt="Next day" src="https://user-images.githubusercontent.com/112055062/192150020-a2d0c895-643d-45e5-85cf-bf7045f120fb.png">

## Linear equation

Write a program that solves a linear equation ax = b in integers. Given two integers a and b (a may be zero), print a single integer root if it exists and print "no solution" or "many solutions" otherwise.

```.py
a = int(input())
b = int(input())
if a == 0:
    output = "no solution"
if b == 0:
    output = "many solutions"
if a != 0 and b!=0:
    output = int(b /a)
    if output == 0:
        output = "no solution"
print(output)
```

Image of the result

<img width="336" alt="linear equation" src="https://user-images.githubusercontent.com/112055062/192484871-65206de3-7ddd-4033-9976-d82ceb921a9c.png">

## Vertices of rectangle

Given integer coordinates of three vertices of a rectangle whose sides are parallel to the coordinate axes, find the coordinates of the fourth vertex of the rectangle. In the first test the three given vertices are (1, 4), (1, 6), (7, 4). The fourth vertex is thus (7, 6).

```.py
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
if x1 == x2:
    x4 = x3
elif x2 == x3:
    x4 = x1
elif x3 == x1:
    x4 = x2
print(x4)
   
if y1 == y2:
    y4 = y3
elif y2 == y3:
    y4 = y1
elif y3 == y1:
    y4 = y2
print(y4)
```

Image of the result

<img width="373" alt="Vertices of rectangle" src="https://user-images.githubusercontent.com/112055062/192500525-3b3048b3-996d-47c7-a9ec-b07d18ef4ae9.png">

## Sort three numbers

Given three integers, print them in ascending order.

```.py
a = int(input())
b = int(input())
c = int(input())
if a<b<c:
    print(a)
    print(b)
    print(c)
if a<c<b:
    print(a)
    print(c)
    print(b)
if b<a<c:
    print(b)
    print(a)
    print(c)
if b<c<a:
    print(b)
    print(c)
    print(a)
if c<a<b:
    print(c)
    print(a)
    print(b)
if c<b<a:
    print(c)
    print(b)
    print(a)
if a==b and b<c:
    print(a)
    print(b)
    print(c)
if a==b and c<b:
    print(c)
    print(a)
    print(b)
if a==c and a<b:
    print(a)
    print(c)
    print(b)
if a==c and b<a:
    print(b)
    print(a)
    print(c)
if b==c and c<a:
    print(b)
    print(c)
    print(a)
if b==c and a<c:
    print(a)
    print(b)
    print(c)
if a==b and b==c:
    print(a)
    print(b)
    print(c)
```

Image of the result:

<img width="368" alt="sort three numbers" src="https://user-images.githubusercontent.com/112055062/192510597-5e9ab1d6-1ea4-45b1-95d5-7d32c24aa014.png">

## Count to N

Given an integer N, print all the numbers from 1 to N.

```.py
N = int(input())
for i in range(1,N+1):
    print(i)
```

Image of the result

<img width="229" alt="count to N" src="https://user-images.githubusercontent.com/112055062/192561349-33f61978-9f20-40ea-8a3e-0689e1067d7d.png">

## Series - 1

Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.

```.py
A = int(input())
B = int(input())
for i in range(A,B+1):
    print(i)
```

Image of the result

<img width="191" alt="Series - 1" src="https://user-images.githubusercontent.com/112055062/192562673-5df93749-98d6-4711-8180-66d48e09a3bb.png">

## First N odd, ascending

Given an integer N, print all the odd numbers from 1 to N in ascending order.

```.py
N = int(input())
for i in range(1,N+1,2):
    print(i)
```

Image of the result

<img width="251" alt="First N odd, ascending" src="https://user-images.githubusercontent.com/112055062/192564233-c656c3c6-70b5-4e53-a302-809b4fae0a4b.png">

## Series - 2

Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B.

```.py
A = int(input())
B = int(input())
if A<B:
    for i in range(A,B+1):
        print(i)
if A>=B:
    for i in range(A,B-1,-1):
        print(i)
```

Image of the result

<img width="194" alt="Series - 2" src="https://user-images.githubusercontent.com/112055062/192567483-c407af37-ea5b-473c-b317-5f20d2a78acc.png">

## First N even, descending

Given an integer N, print all the even numbers from 0 to N in descending order.

```.py
N = int(input())
if N%2==0:
    for i in range(N,-1,-2):
        print(i)
else:
    for i in range(N-1,-1,-2):
        print(i)
```

Image of the result

<img width="280" alt="First N even, descending" src="https://user-images.githubusercontent.com/112055062/192568928-da0663bb-73da-44a3-b1fa-e7196786892a.png">

## Sum of ten numbers

10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.

```.py
sum = 0
for number in range(10):
    sum += int(input())
print(sum)
```

Image of the result

<img width="224" alt="Sum of ten numbers" src="https://user-images.githubusercontent.com/112055062/192571279-300725fc-5e3c-44ae-be94-854d1d7a0911.png">

## Sum of N numbers

N numbers are given in the input. Read them and print their sum.
The first line of input contains the integer N, which is the number of integers to follow. Each of the next N lines contains one integer. Print the sum of these N integers.

```.py
N = int(input())
sum = 0
for i in range(1,N+1):
    sum += int(input())
print(sum)
```

Image of the result

<img width="339" alt="Sum of N numbers" src="https://user-images.githubusercontent.com/112055062/192572760-9b641620-4b16-422e-b76d-7ea0a30e6635.png">

## Product of N numbers

N numbers are given in the input. Read them and print their product.
The first line of input contains a positive integer N: the number of integers to follow. Each of the next N lines contains one integer. Print the product of these N integers.

```.py
N = int(input())
product = 1
for i in range(1,N+1):
    product *= int(input())
print(product)
```

Image of the result:

<img width="285" alt="Product of N numbers" src="https://user-images.githubusercontent.com/112055062/192574592-0a479146-abac-4aa2-8376-8706feb14b3e.png">

## Sum of cubes

For the given integer N calculate the following sum:
13+23+…+N3

```.py
N = int(input())
all = 0
for i in range(1,N+1):
    all += i**3
print(all)
```

Image of the result

<img width="340" alt="Sum of cubes" src="https://user-images.githubusercontent.com/112055062/192575297-e46d8cbb-6b93-4aa6-ac46-b6f698dff444.png">

## Factorial

In mathematics, the factorial of an integer n, denoted by n! is the following product:
n!=1×2×…×n
For the given integer n calculate the value n!. Don't use math module in this exercise.

```.py
n = int(input())
n_fact = 1
for i in range(1,n+1):
    n_fact *= i
print(n_fact)
```

Image of the result

<img width="372" alt="Factorial" src="https://user-images.githubusercontent.com/112055062/192575962-c798d5f6-25dc-40a7-9002-0ccbdeee9e9d.png">

## The number of zeros

Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it.
You need to count the number of numbers that are equal to zero, not the number of zero digits.

```.py
N = int(input())
count = 0
for i in range(1,N+1):
    number = int(input())
    if number == 0:
        count += 1
print(count)
```

Image of the result

<img width="258" alt="The number of zeroes" src="https://user-images.githubusercontent.com/112055062/192578232-608ca453-96bf-495a-b34a-85e70fa4515c.png">

## Adding factorials

Given an integer n, print the sum 1!+2!+3!+...+n!.
This problem has a solution with only one loop, so try to discover it. And don't use the math library :)

```.py
n = int(input())
sum = 0
factorial = 1

for i in range(n):
    i += 1
    factorial *= i
    sum += factorial
print(sum)
```

Image of the result

<img width="308" alt="Adding factorials" src="https://user-images.githubusercontent.com/112055062/192580139-de8964bc-c54c-4f97-87f7-9a3c91220f20.png">

## Squares in range

Given two integers A and B, print squares of all integer numbers between them, as shown below. There shouldn't be any spaces around * and =. The sep argument of the function print() may help you with that.

```.py
A = int(input())
B = int(input())
for i in range(A,B+1):
    print(str(i)+"*"+str(i)+"="+str(i*i))
```

Image of the result

<img width="251" alt="Squares in range" src="https://user-images.githubusercontent.com/112055062/192584865-3d04239f-6aac-448b-b144-c6b58fbd4ae4.png">

## Ladder

For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.
To do that, you can use the sep and end arguments for the function print().

```.py
n = int(input())
count = ""
for i in range(1,n+1):
    count += str(i)
    print(count)
```

Image of the result

<img width="293" alt="Ladder" src="https://user-images.githubusercontent.com/112055062/192587896-54523d4e-09cc-41f4-accc-99f3d48081c0.png">

## Is prime

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given an integer N > 1, print PRIME if it's prime and print COMPOSITE otherwise.

```.py
N = int(input())
out = "PRIME"
for i in range(2, N):
    if N % i == 0:
        out = "COMPOSITE"

print(out)
```

Image of the result

<img width="411" alt="Prime" src="https://user-images.githubusercontent.com/112055062/192592228-bef898d3-31f2-40b5-a6fb-f63ff2a62b61.png">

## Print primes in range

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given two integers A and B, print all prime numbers between them, inclusively.

```.py
A = int(input())
B = int(input())
for i in range(A,B+1):
    if i > 1:
        for x in range(2,i):
            if i%x == 0:
                break
        else:
            print(i)
```

Image of the result

<img width="382" alt="Print primes in range" src="https://user-images.githubusercontent.com/112055062/192595359-c0660534-6468-468e-a38a-1c054a34f9e1.png">

## Number of primes in range

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Given two integers A and B, print the number of primes between them, inclusively.



# Quiz 015

<img width="569" alt="quiz 015 " src="https://user-images.githubusercontent.com/112055062/194758668-c1d9618b-1ea8-418f-b301-802bf5dec1a7.png">


```.py
def open_doors(num_students:int)->int:
    doors = []
    d = 0
    for n in range(num_students):
        doors.append(False)
    for d in range(1,num_students+1):
        for stu in range(1,num_students+1):
            if d % stu==0:
                 doors[d-1] = not doors[d-1]
    count = 0
    for i in doors:
        if i == True:
            count += 1

    print(count)

input = int(input("please input the number of students"))
open_doors(input)
```

<img width="700" alt="quiz 015 result" src="https://user-images.githubusercontent.com/112055062/194758696-763781e3-ab79-4409-a671-f1492789d09c.png">

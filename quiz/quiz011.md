# Quiz 011
```.py
def bestMonth(month)->str:
    if month == "January":
        out = """
               January 2022
        Mon Tue Wed Thu Fri Sat Sun
                             1   2
         3   4   5   6   7   8   9
        10  11  12  13  14  15  16
        17  18  19  20  21  22  23
        24  25  26  27  28  29  30
        31
        
        """

    if month == "February":
        out = """
               February 2022
        Mon Tue Wed Thu Fri Sat Sun
             1   2   3   4   5   6
         7   8   9  10  11  12  13
        14  15  16  17  18  19  20
        21  22  23  24  25  26  27
        28
        """

    if month == "March":
        out = """
                March 2022
        Mon Tue Wed Thu Fri Sat Sun
             1   2   3   4   5   6
         7   8   9  10  11  12  13
        14  15  16  17  18  19  20
        21  22  23  24  25  26  27
        28  29  30  31    
        """

    if month == "April":
        out = """
                April 2022
        Mon Tue Wed Thu Fri Sat Sun
                         1   2   3
         4   5   6   7   8   9  10
        11  12  13  14  15  16  17
        18  19  20  21  22  23  24
        25  26  27  28  29  30                 
        """

    if month == "May":
        out = """
                May 2022
        Mon Tue Wed Thu Fri Sat Sun
                                 1
         2   3   4   5   6   7   8
         9  10  11  12  13  14  15
        16  17  18  19  20  21  22
        23  24  25  26  27  28  29
        30  31                      
        """

    if month == "June":
        out = """
                June 2022
        Mon Tue Wed Thu Fri Sat Sun
                 1   2   3   4   5
         6   7   8   9  10  11  12
        13  14  15  16  17  18  19
        20  21  22  23  24  25  26
        27  28  29  30  
        """

    if month == "July":
        out = """
                July 2022
        Mon Tue Wed Thu Fri Sat Sun
                         1   2   3
         4   5   6   7   8   9  10
        11  12  13  14  15  16  17
        18  19  20  21  22  23  24
        25  26  27  28  29  30  31
        """
    if month == "August":
        out = """
                August 2022
        Mon Tue Wed Thu Fri Sat Sun
         1   2   3   4   5   6  7
         8   9  10  11  12  13  14
        15  16  17  18  19  20  21
        22  23  24  25  26  27  28
        29  30  31
        """

    if month == "September":
        out = """
                September 2022
        Mon Tue Wed Thu Fri Sat Sun
                     1   2   3   4
         5   6   7   8   9  10  11
        12  13  14  15  16  17  18
        19  20  21  22  23  24  25
        2ุ6  27  28  29  30        
        """
        
    if month == "October":
        out = """
                October 2022
        Mon Tue Wed Thu Fri Sat Sun
                             1   2
         3   4   5   6   7   8   9
        10  11  12  13  14  15  16
        17  18  19  20  21  22  23
        24  25  26  27  28  29  30
        31
        """

    if month == "November":
        out = """
                November 2022
        Mon Tue Wed Thu Fri Sat Sun
             1   2   3   4   5   6
         7   8   9  10  11  12  13
        14  15  16  17  18  19  20
        21  22  23  24  25  26  27
        28  29  30
        """

    if month == "December":
        out = """
        Mon Tue Wed Thu Fri Sat Sun
                     1   2   3   4
         5   6   7   8   9  10  11
        12  13  14  15  16  17  18
        19  20  21  22  23  24  25
        2ุ6  27  28  29  30  31
        """
    return out

month_input = input("please enter month ")
test1 = bestMonth(month_input)
print(test1)
```

![quiz011](https://user-images.githubusercontent.com/112055062/194769456-46df2e54-73bc-4e1f-abfc-de09e0dff058.jpg)


<img width="446" alt="Quiz 011 result" src="https://user-images.githubusercontent.com/112055062/194769485-fd17a5af-c6b5-4087-b7d3-d61fbbc803ef.png">

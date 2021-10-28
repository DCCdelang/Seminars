from assignment_2b import function_2b
from assignment_2c import function_2c
"""
Used the imported functions (function_2b and function_2c) and the documentation
provided by your teammates to generate the correct answers below. You can use
the following numbers and strings as input for the 2 functions:
[5, 10, 100, 1000, -50, 'seminars', 'Seminars', 'CLS', 'cLs', 'Borrel']
Run the script to see if you succeeded! PS: Multiple combinations are possible,
just give a correct one.
"""


"""

function_2b(string_1, string_2)
Arguments - string_1 and string_2
Return value - dictionary
Key value pairs for the dictionary are as follows - 
Key | value
'L' | string_1 in lower case letters
'U' | string_2 in upper case letters
'C' | string_2 appended to string_1 (string_1 + string_2)

"""

"""

function_2c(w,x,y,z)
Return value - dictionary with key value pairs
key -> algebraic operations("multiply","divide","add","subtract")
values -> x*y,x/y,w+z,w-z

""""



var_1 = function_2b(...)

var_2 = function_2c(...)

var_3 = str(function_2b(...)) + function_2c(...)

if var_1 == 950:
    print("Good job!")

if var_2 == "SeminarsBorrel":
    print("Well done!")

if var_3 == "10000cls":
    print("Excellent!")

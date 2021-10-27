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

number = [5, 10, 100, 1000, -50]
string =  ['seminars', 'Seminars', 'CLS', 'cLs', 'Borrel']

var_2 = function_2b(string[1], string[4])["C"]

var_1 = function_2c(number[3], number[1], number[2], number[4])["add"]

var_3 = str(function_2c(number[1], number[1], number[3], number[3])["multiply"]) + str(function_2b(string[3], string[3])["L"])

if var_1 == 950:
    print("Good job!")

if var_2 == "SeminarsBorrel":
    print("Well done!")

if var_3 == "10000cls":
    print("Excellent!")

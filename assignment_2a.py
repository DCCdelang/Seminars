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

var_1 = int(function_2b("1000", "-50")["L"]) + int(function_2b("1000", "-50")["U"])

var_2 = function_2c(4, 3, 2, 1)

var_3 = str(function_2b("1000", "100")["L"]) + str(function_2c(4,3,2,1)["multiply"])

if var_1 == 950:
    print("Good job!")

if var_2 == "SeminarsBorrel":
    print("Well done!")

if var_3 == "10000cls":
    print("Excellent!")



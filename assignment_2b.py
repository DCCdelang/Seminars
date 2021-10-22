"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
"""
function_2b arguments: string_1, string_2 in this order
does the following:
-turns string_1 to lowercase and store it to a variable named "lower"
-turns string_2 to uppercase and stores it to a variable named "upper"
-combines string_1 and string_2 with no blank spaces and store it to a
variable named "combined"

returns a dictionary with the following key-value pairs:
"L": lower
"U": upper
"C": combined
"""
def function_2b(string_1, string_2):
    
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

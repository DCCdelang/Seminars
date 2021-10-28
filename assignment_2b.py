"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
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




def function_2b(string_1, string_2):

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

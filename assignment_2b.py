"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
## DOCS ###

# Function 2b can be used to modify strings. It takes two strings as input, and returns a dictionary with the lower case version
# of the first input string, corresponding to the key L. Moreover, it returns the upper case version of the second input string,
# corresponding to the dictionary key U and lastly it returns combined version of both strings.
# So, it concatenates (the lower case) the first input string and the (upper case) second input string.



def function_2b(string_1, string_2):

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

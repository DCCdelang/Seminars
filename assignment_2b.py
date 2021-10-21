"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""


def function_2b(string_1, string_2):

    """
    It is a magical function that takes two strings, and returnes a dictionary, in which:
    the first key is the first string (input) is in lower case, 
    the second key is the string (input) is in upper case, and 
    and the third key is a combinations of two. 
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

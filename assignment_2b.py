"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    The function takes string_1 and string_2 and converts them in respectively lower and upper case. 
    A dictionary will be returned with "L" as key for the lowercase string_1 and "U" for uppercase string_2.
    A third key is added "C" for the combined strings (lowercase string_1 + uppercase string_2).
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

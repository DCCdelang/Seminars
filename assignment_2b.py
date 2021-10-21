"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
        Requires to arguments: string 1 and string 2. Returns a dict.
        "L" gives the lower of string 1, "U" gives the upper of string 2, "C" gives the combination of string 1 and string 2
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

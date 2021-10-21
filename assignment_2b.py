"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Argument:
    string1 -- text you want to turn into lower case
    string2 -- text you want to turn into upper case

    Returns:
    dict -- dictionary with:
            1. lower case version of string1
            2. upper case version of string2
            3. combination of string1 and string2
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):

    """
    Argument:
    string_1 -- string
    string_2 -- string

    Returns:
    dictionary {
        "L": lower case version of string_1,
        "U": upper case version of string_2,
        "C": combines string_1 and string_2
    }
    
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dictionary = {"L": lower,
               "U": upper,
               "C": combined}

    return dictionary

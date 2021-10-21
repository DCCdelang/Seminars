"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Creates a lowercase version of string1 and an uppercase version of string2
    and returns a dict with lowercase, uppercase and combined.
    Arguments:
        string_1 -- text you want to turn into lowercase
        string_2 -- text you want to turn into uppercase
        
    Returns:
        dict -- dictionary of "L": lowercase, "U": uppercase 
        and "C": lowercase + uppercase
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

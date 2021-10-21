"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Transform the first string to lower case and the second to upper case.
    Also, concatenate the original strings (without a space) and create a 
    dictionary with the two transformed strings and the concatenated string.

    Arguments:
    string_1 -- string to transform to lower case
    string_2 -- string to transform to upper case

    Returns:
    a dictionary with keys "L", "U" and "C" corresponding to the lower case
    string, upper case string and concatenated string.
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """Perform some basic string manipulations
    Arguments:
        string_1    The first string
        string_2    The second string

    Returns:
        Dictionary containing the following keys:
        L   Lower case representation of the first string
        U   Upper case representation of the second string
        C   The first string and the second string concatenated
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """[You send the function two strings, it takes the first making it all lower case, takes the second and makes it all upper case,
    create a third string which combines the two. Store the lowercase, uppercase and combined string in a dictionary]

    Args:
        string_1 ([str]): [random string]
        string_2 ([str): [random string]

    Returns:
        [Dictionary]: [key = L: Storing upper case of string 1, key = U: storing string 2 lower case, key = C: for combined string of upper and lower case]
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

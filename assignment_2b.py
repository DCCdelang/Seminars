"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    given parameters
    string_1 : string given as first given parameter
    string_2 : string given as second given parameter

    parameters made in function
    lower : First string parameter in lower cases
    upper: Second string parameter in upper cases
    combined : A string of string_1 and string_2 combined

    returned values:
    dict : is a dictionary with keys "L", "U" and "C" with values lower, upper and combined
    respectively
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}
    return dict

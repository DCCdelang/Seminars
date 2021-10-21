"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Calculate basic arithmetic operations (multiplication, division, addition
    and subtraction). Calculates x*y, x/y, w+z and w-z and returns them as
    a dictionary.

    Arguments:
    w, x, y, z -- Numbers to use for calculations

    Returns:
    A dictionary with keys 'multiply', 'divide', 'add' and 'subtract' which
    map to the corresponding values.
    """


    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results

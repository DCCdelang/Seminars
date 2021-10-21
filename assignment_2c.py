"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """ Performs multiplication, division, addition and subtraction on the input values. 
    Parameters
    ----------
    w
    A value to either add to z or from which z is subtracted
    x
    A value to either multiply by value y or which is divided by y
    y 
    A value to either multiply by value x or divide x by
    z 
    A value to add to w or to subtract from w

    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    Returns
    -------
    A dictionary containing the results to the four mathematical operations on the values, with keys 
    "multiply", "divide", "add", "subtract". 
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

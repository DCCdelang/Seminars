"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """

    Argument:
    w, x, y, z -- variables you want to multiply, divide, add, substract

    Returns:
    results -- Dictionary with results of x multiplied by y, x divided by y, 
    addition of w and z, z substracted from w 

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

    nump = function_2c("w", "x", "y", "z")

    print(numby["multiply"])

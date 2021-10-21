"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """Perform some basic arithmetic
    Arguments:
        w,x,y,z     Numbers to perform calculations on

    Returns:
        Dictionary containing the following keys:
        multiply    x * y
        divide      x / y
        add         w + z
        subtract    w - z
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

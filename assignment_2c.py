"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""



def function_2c(w, x, y, z):

    """
    Of the input variables w, x, y, z (integers) it returns a multiplication and division of x and y, and, 
    a addition and subtraction of w and z, in that order. (x*y), (x/y), (w + z) (w - z)
     The output is a string. 
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

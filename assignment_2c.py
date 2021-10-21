"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Requires 4 numbers (in order): w, x, y and z. Returns dict.
    "multiply" gives the multiplication of x an y.
    "divide" gives x divided by y
    "add" gives adds w and z
    "subtract" gives the subtaction of w by z
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

"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Multiplies x and y, divides x and y, adds up w and z and subtracts w and z 
    and returns a dict with all of them.
    
    Arguments:
        w -- number which you want to add up and subtract
        x -- number which you want to multiply and divide
        y -- number which you want to multiply and divide
        z -- number which you want to add up and subtract
        
    Returns:
        results -- dictionary of "multiply": x * y, "division": x / y, 
        "add": w + z and "subtract": w - z
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

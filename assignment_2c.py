"""
This function performs mathematic operations on the given (4) integers. 
It multiplies and divides the second and third arguments, and it adds and substracts the first and last arguments. 
It returns a dictionary with the results of each operation. 
"""
def function_2c(w, x, y, z):
    """
    Argument:
    z -- int

    x -- int

    y -- int

    z -- int

    Returns:
    results -- dictionary of the results of all operations
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

"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """Creates dictionary with the simple computations: Multiply x and y; Divide X by y; add w and z and finaly substract z from w. The values of th
    computation can be received by using the following keys:
    "muliply" for multiplication,
    "divide" for division,
    "add" for addition,
    "substract" for substraction

    Args:
        w (number): winston
        x (number): Xiavier
        y (number): Yusef
        z (number): Zorro

    Returns:
        dict: dictionary with the values
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

"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
"""
function_2c arguments: w, x, y, z in this order
doe the following:
-multiplies x with y and stores the result to a variable named "multiplication"
-divides x by y and stores the result to a variable named "division"
-adds w and z and stores the result to a variable named "addition"
-subtracts z from w and stores the result to a variable named "subtraction"

returns a dictionary with the names of the abovementioned verbs
(multiply, divide, add, subtract) as keys and the result of
the abovementioned computations as values
"""
def function_2c(w, x, y, z):
    
    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results

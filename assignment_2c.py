def function_2c(w, x, y, z):
    """
    Description
    -----------
    Function takes 4 floats/integers and returns some 
    arithmetic results of combining them in different ways
    
    Input
    -----
    w: float
    x: float
    y: float
    z: float

    Returns
    -------
    results: dict
            dictionary keys
            'multiply': multiply of x,y
            'divide': devide x by y
            'add': add w,z
            'subtract': subtract z from w
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

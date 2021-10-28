def function_2b(string_1, string_2):
    """
    Description
    -----------
    Function takes two strings and returns 3 variations of it in dictionary

    Input
    -----
    string_1: str
    string_2: str

    Output
    ------
    dict: dicitonary
            dictionary keys: 
                "L": string_1 in lower case  
                "U": stromg_2 in upper case 
                "C": combination (additive) of string_1, string_2
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict

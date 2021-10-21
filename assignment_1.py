"""
In this short exercise you will practice dealing with a merge conflict.
Finish the lower_case function and push your changes to the Github repository.
The fastest one to push is lucky, the others will most likely get a merge
conflict. See if you can fix it :)
"""

def lower_case(string):
    """
    Argument:
    string -- text you want to turn into lower case

    Returns:
    lower_string -- lower case version of string

    """

    ### your code starts here
<<<<<<< HEAD
    lower_string = string.lower() # my version
=======
    lower_string = string.lower()
>>>>>>> 865349541354151e091359da1ce91502f1bd0744
    ### your code ends here

    return lower_string


"""
Do the same thing again with upper_case, but change the order so everyone
experiences at least 1 merge conflict.
"""

def upper_case(string):
    """
    Argument:
    string -- text you want to turn into upper case

    Returns:
    upper_string -- upper case version of string
    
    """

    ### your code starts here
<<<<<<< HEAD
    upper_string = string.upper()
=======
    lower_string = string.upper()
>>>>>>> 865349541354151e091359da1ce91502f1bd0744
    ### your code ends here

    return upper_string

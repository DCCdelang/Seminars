# Seminars
Assignment for Seminars Lecture on Team-based Coding Projects

Instructions:
1. Fork this repository.

2. Add your group member(s) as collaborators to your repo

3. Do the assignment (together):
Clone the repository to your workstation and open assigment_1.py in your favorite editor (all group members). Follow the instructions in the script.
When you are finished, you split up for assignment 2. One of you opens 2a, the other two do 2b and 2c (if you are a group of two, the same person does 2b and 2c).
Everyone follows the instructions in their script. Once you have pushed all your changes, continue.

4. Create a pull request for me to this (original) repo. (Hint: you can use the "New pull request" button and then do a "compare across forks").

## Documentation

### assignment_2b.py
This file holds a function named `function_2b` which takes two string parameters.
The output of this function is a dictionary with four keys and their respective values:
* `L` - the first string in lower case
* `U` - the second string in upper case
* `C` - the concatenation of the two strings

Try it out in your own terminal with the below example:

```
> python
> from assignment_2b import function_2b
> dict = function_2b('ONE', 'two')
> print(dict.values())
> print(dict['L'])
```

### assignment_2c.py
This file holds a function named `function_2c` which takes four integer parameters.
The output of this function is a dictionary with four keys and their respective values:
* `multiply` - second * third
* `divide`   - second / third
* `add`      - first + fourth
* `subtract` - first - fourth

Try it out in your own terminal with the below example:

```
> python
> from assignment_2c import function_2c
> dict = function_2c(1, 2, 3, 4)
> print(dict.values())
> print(dict['add'])
```

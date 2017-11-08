#!/usr/bin/python

'''
Platform Engineer Training - Part 1
W2D2 - flow control, sequences, and iterables

Exercises related to: Sequences and Iterables

Pro-tip: run a specific function from the command line directly like so:
python -c 'import this_filename; my_function(a_parameter,b_parameter)'
(you must be in the directory where "this_filename.py" resides)

'''

# Place any needed module imports here...
# Example: import modulename as mn

# Please see the "Sequences and Iterables Exercises" portion of
# pairedexercises.md from today's class directory for further information.


def alpha_ranger():
    '''
    Use your knowledge of flow control and one of the built-in functions
    'range' or 'xrange' to populate a list or string with all lower and
    uppercased letters from 'a' to 'z'.

    Hint: Take a look at python's 'string' module
    '''

def meta_dictionary():
    '''
    Complete this function such that - when given a sequence of dictionaries
    with an "id" attribute - it builds a new dictionary mapping IDs to the
    dictionaries themselves.
    '''

def timespan_dicts():
    '''
    Utilize a dictionary-based matching strategy to complete this function.

    When provided an integer and a string representing a length of time
    (the string being one of either 'second', 'minute', or 'hour'), this
    function shall return a timespan object (known in python as a timedelta)
    equivalent to the value passed in via string and integer combination.

    Hint: Take a look at python's 'datetime' module. It is expansive, so an
    HTML/browser-based documentation source is recommended for new python
    programmers over the help() function due to readability constraints.

    Example input :
    amount = 30
    units  = "hours"

    Example output from calling timespan_dicts(amount,units):
    1 day, 6:00:00
    '''

def main():
    '''
    For extra points, modify this main function to call your
    other completed functions.

    You may statically define the function parameters that are
    passed in for each function call, or utilize a module to
    grab arbitrary parameters from the command line invocation.

    Either is perfectly valid.
    '''

# Keep this as-is to invoke main.
if __name__ == '__main__':
    main()

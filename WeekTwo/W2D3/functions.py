#!/usr/bin/python

'''
Platform Engineer Training - Part 1
W2D2 - functions, arguments, and decorators

Exercises related to: functions and arguments

Pro-tip: run a specific function from the command line directly like so:
python -c 'import this_filename; my_function(a_parameter,b_parameter)'
(you must be in the directory where "this_filename.py" resides)

'''

# Place any needed module imports here...
# Example: import modulename as mn

def arbitrary_args():
    '''
    Define a function taking in an arbitrary number of arguments and
    returning the item of these arguments with the longest length (“len” function)
    Accept and filter out items that do not support the “len” operation
    '''

def debug_logger():
    '''
    Instantiate a “logger” from the python standard library and call “.debug”
    on it using a message and the following dictionary:
    {‘exc_info’=0, ‘extra’={'clientip': '192.168.0.1', 'user': ‘admin’}}
    '''

def order_keywords():
    '''
    Define a function that will accept keyword arguments and put them into an
    ordered dictionary in alpha order and return the dictionary
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

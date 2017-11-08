#!/usr/bin/python

'''
Platform Engineer Training - Part 1
W2D2 - functions, arguments, and decorators

Exercises related to: decorators

Pro-tip: run a specific function from the command line directly like so:
python -c 'import this_filename; my_function(a_parameter,b_parameter)'
(you must be in the directory where "this_filename.py" resides)

'''

# Place any needed module imports here...
# Example: import modulename as mn

def classproperty():
    '''
    Define a decorator, “classproperty”, mimicking the behavior of classmethod
    and property combined (a method that can be called like a property with the
    class passed in as the first argument)
    '''

def lazyproperty():
    '''
    Define a decorator, “lazyproperty”, which will evaluate the value of the
    method body once for the instance and then store it in a backing field so
    that it does not have to be evaluated again
    '''


# Keep this as-is to invoke main.
if __name__ == '__main__':
    main()

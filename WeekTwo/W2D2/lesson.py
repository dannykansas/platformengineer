#!/usr/bin/python

'''
Platform Engineer Training - Part 1
W2D2 - flow control, sequences, and iterables

Pro-tip: run a specific function from the command line directly like so:
python -c 'import this_filename; my_function(a_parameter,b_parameter)'
(you must be in the directory where "this_filename.py" resides)

'''

# Place any needed module imports here...
import boilerplate as bpl

# Example 0: A few variables of various data types
# Purpose: These are global and available to all functions, so we can easily
#   reference them anywhere and save time typing while also keeping our code
#   nice and readable. See opening comment for usage specifics / examples...
ex_string = "Example String"
ex_integer = 15
ex_list = ['this','is','a','list','of','strings']
ex_list_of_tuples = [(1,1),(2,4),(3,9),(4,16)]
ex_dict = {
    "key_one":   1,
    "key_two":   2,
    "key_three": 3,
    "key_four":  4,
}

# Example Group One: flow control, tuple, namedtuple
# This group contains several functions illustrating various methods for
# controlling flow in Python. This is a brief overview and far from definitive.
# More here: http://en.wikibooks.org/wiki/Python_Programming/Control_Flow

# Example 1: 'if' statements
# Purpose: Simple 'if' statement with 'elif' and 'else'.
#   Only accepts integers (no 'float', 'complex', or other datatypes than 'int')
def control_flow_if(ex_integer):
    if isinstance(ex_integer,int):
        if ex_integer > 0:
            print "Value was Positive"
        elif ex_integer == 0:
            print "Value was Zero"
        elif ex_integer < 0:
            print "Value was Negative"
    else:
        print "I don\'t think you entered an integer..."

# Example 2: 'for' loops
# Simple 'for' loop iterating over an arbitrary input
# each element of the list (i.e. each letter in a string)
def control_flow_simple_for(ex_string):
    for i in ex_string:
        print i

# Example 3: More 'for' loops with multi-tuple list
# Definition: Loops through a list of two-element tuples
# Note: A tuple is simply an immutable (unchangeable) list
#   Tuples are defined with parentheses "()"
#   Lists are defined with brackets "[]"
def control_flow_tuple_for(ex_list_of_tuples):
    for i, isquared in ex_list_of_tuples:
        print i, ":", isquared

# Example 4: 'while' loops
# A function illustrating various usages of controlling flow
# with python's built-in control flow statements
def control_flow_simple_while(ex_list):
    i = 0
    while i < len(ex_list):
        print ex_list[i]
        i += 1
    else:
        print "Done."

# Boilerplate message if invoked without function explicitly called
def main():
    print bpl.usage_notify()

# Again, ignore this for now (unless you want to change the default function
# invocation from main() to something else...)
if __name__ == '__main__':
    main()

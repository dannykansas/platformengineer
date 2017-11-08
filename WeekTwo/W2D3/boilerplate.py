#!/usr/bin/python

'''
Platform Engineer Training - Part 1

Boilerplate Formatting Functions

Written by Dan Fowler, technically, but primarily lifted from PEP-257:
https://www.python.org/dev/peps/pep-0257/#handling-docstring-indentation

'''

import sys

def usage_notify():
    _notify_copy = """
    This module is primarily designed to be imported by an interactive Python
    interpreter as part of a larger teaching series.

            Please view the GitHub repository for more info:

            https://github.com/dannykansas/platformengineer
    """
    return trim(_notify_copy)


def trim(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxint
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxint:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)

if __name__ == '__main__':
    if len(sys.argv) != 1:
        happy_string = trim(sys.argv[1])
        print happy_string
    else:
        usage_string = "Usage: boilerplate.py 'very long string needing to be nicely formatted'"
        print usage_string

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            # this %(key,value) part seems to be some syntax
            # for substituting variables in dynamically
            print "%s == %s" %(key,value)
    else:
        print "I did not get a kwarg!"

def just_print(**kwargs):
    if kwargs is not None:
        print "kwargs is not None"
        print kwargs
    else:
        print "kwargs is None"

def not_predefined(myarg1,myarg2,myarg3):
    print "arg1: ", myarg1
    print "arg2: ", myarg2
    print "arg3: ", myarg3

def overload_nodefine(myarg1,myarg2):
    print "arg1: ", myarg1
    print "arg2: ", myarg2

# integers
myintegers = (1,2,3)
# strings
mystrings = ("one","two","three")
# mixed
mymix = (1,"two",3)
# mixed with other variable
othervar = "three"
myothermix = (1,2,othervar)

# NOTE: this works beautifully when *args is used
# NOTE: you just prepend "*" to the variable name
# NOTE: and ensure it has exactly the number of values that the function takes
not_predefined(*myothermix)

# NOTE: this breaks with "taxes exactly x arguments (y given)"
#overload_nodefine(*myintegers)

greet_me(potato="potato")
greet_me(potato="but",tomato="what")

# NOTE: This doesn't cause the "else" statement to fire, which is interesting
#greet_me()

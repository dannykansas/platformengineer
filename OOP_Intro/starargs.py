import string

def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

def _var_generator():
    v = 20
    print "I want %s arguments" % v
    string.ascii_lowercase


test_var_args('yasoob','python','eggs','test')

print string.ascii_letters
print list(string.punctuation)

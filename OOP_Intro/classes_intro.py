# This is just a simple intro to:
# Classes
# Class instances
# Instance methods
# Class methods
# Alternative costructors, and static methods
class Employee():

    # CLASS VARIABLES are shared
    # across ALL INSTANCES OF THE CLASS
    emp_count = 0
    raise_amount = 1.04


    def __init__(self, first, last, pay):
       # these are INSTANCE VARIABLES and
       # they change WITH EACH INSTANCE OF THE CLASS
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

        Employee.emp_count += 1

    # REGULAR METHODS take the instance (self) as the first arg
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Another regular method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class methods take the class as the first arg
    # use a @classmethod decorator to create
    # convention is: cls
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # alternative constructor example
    # this allows adding employees in the format:
    # "Dan-Howler-160000"
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # STATIC METHODS
    # Behave just like regular functions but have some sort
    # of logical connections with the class itself
    # default: nothing
    # uses: @staticmethod decorator
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# alternative constructor utilization

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Jane-Doe-80000'
emp_str_3 = 'Jane-Don-60000'

new_emp_1 = Employee.from_string(emp_str_1)

print new_emp_1.email
print new_emp_1.fullname()

# emp_count is a Class variable (as opposed to an instance variable)
# a Class variable makes sense here because it never differs between
# which employee you are accessing (although it can and will be iterated
# by new Employee instances as seen below)

# print Employee.emp_count

emp_1 = Employee('Dan','Howler', 160000)
emp_2 = Employee('Test','Employee', 185000)

# this uses the class method set_raise_amt()
# to modify the actual Class variable instead of just the instance variable
# cool!

# Employee.set_raise_amt(1.05)

#print Employee.raise_amount
#print emp_1.raise_amount
#print emp_2.raise_amount

import datetime
my_date = datetime.date(2017, 11, 7)
print Employee.is_workday(my_date)

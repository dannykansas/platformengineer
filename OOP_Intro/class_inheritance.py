class Employee():

    emp_count = 0
    raise_amount = 1.04


    def __init__(self, first, last, pay):
       # INSTANCE VARIABLES
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

        Employee.emp_count += 1

    # REGULAR METHOD
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Another regular method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        print "{} manages:".format(self.fullname())
        for emp in self.employees:
            print '-->', emp.fullname()

    # don't set default arg as a mutable type (like a list, that'd be bad)

emp_1 = Employee('Some','Employee',70000)

dev_1 = Developer('James','Smith',125000, 'python')
dev_2 = Developer('Salmon','Montreal',170000, 'haskell')

mgr_1 = Manager('Big', 'Bossmans', 750000, [dev_1])

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

print 'Uh oh. Demotion time for {}'.format(mgr_1.fullname())

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print isinstance(mgr_1, Manager)
#print dev_1.email + " uses " + dev_1.prog_lang
#print dev_2.email + " uses " + dev_2.prog_lang


# Method Resolution Order
#
# use the help() function
# to show this (at the top)

# print(help(Developer))

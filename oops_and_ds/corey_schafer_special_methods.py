
# !

class Employee:

    raise_amount = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname.replace(' ', '')+'.' + \
            lname.replace(' ', '')+'@company.com'

    def fullname(self):
        return '{} {}'.format(self.fname.title(), self.lname.title())

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.fname, self.lname, self.pay)

    def __str__(self):
        return'{} - {}'.format(self.fullname(), self.email)


emp_1 = Employee("Rajasekhar", 'Jamithireddy', 75000)
emp_2 = Employee('hima prathyusha', 'gunupudi', 90000)

print(emp_1)
print(repr(emp_1))
print(str(emp_1))

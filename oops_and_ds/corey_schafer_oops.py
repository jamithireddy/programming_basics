import datetime


class Employee:
    raise_amount = 1.04
    no_of_emp = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname.replace(' ', '')+'.' + \
            lname.replace(' ', '')+'@company.com'

        # This adds  1 to the Variable whenever and employee is added
        Employee.no_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.fname.title(), self.lname.title())

    def apply_raise(self):
        # We have to access the class variable either my class name.variable or through instance as Self.Variable
        self.pay = int(self.pay*Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# This means "emp_1" is an instance created upon the blue print "Employee"(class)
emp_1 = Employee('rajasekhar', 'jamithireddy', 95000)
# Both emp_1 and emp_2 are unique Employee Objects
emp_2 = Employee('hima prathyusha', 'gunupudi', 87000)
emp_3 = Employee('Shankar Prasad', 'Chilamkurthi', 100000)
# Instance variables contain data unique to the instance
# print(emp_1.fullname())
# print(emp_2.fullname())
# print(emp_2.email)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(Employee.no_of_emp)

print("-----------------------------------------------------------------------------------------------------")
#####################################################################################
#                               Class Methods                                      #
###################################################################################
# ! Regular Method: Passes instance(self) automatically as first arguement.
# ! Class Method: Passes Class (cls) as the the first arguement.
# ! Static Method: Passes neither self or class as the first arguement. Though placed in the Class module works as a function.

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

emp4 = Employee.from_string(emp_str_1)
print(emp4.email)
print(emp4.pay)

mydate = datetime.date(2016, 7, 11)

print(Employee.is_workday(mydate))

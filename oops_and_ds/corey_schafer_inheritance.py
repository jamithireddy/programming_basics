
# ! Inheritance allows to inherit all the attributes from the parent class

# Creating a base class employee with first name, last name , pay and email getting auto generated from name
# Also a class variable

class Employee():
    raise_amt = 1.04

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname.replace(" ", "").lower(
        )+"."+lname.replace(" ", "").lower()+'@company.com'

    def full_name(self):
        return self.fname.title()+' '+self.lname.title()

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)


# Creating Developer and Manager Subclasses

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        # Employee.__init__(self,fname,lname,pay)        <-- This shall work as well instead of super. However super should be preferred
        self.prog_lang = prog_lang


dev_1 = Developer('rajasekhar', 'jamithireddy', 50000, 'Python')
dev_2 = Developer('hima prathyusha', 'gunupudi', 70000, '.Net')

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

# In the above we have set employees as None rather than a mutable empty list as we should not initialize an empty list.
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name())


mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.remove_emp(dev_1)
print("----------------------------")
mgr_1.print_emps()

# isinstance() <-- Returns TYrue or False depending upon the instance being a class.

print('Is a Manager: ', isinstance(mgr_1, Manager))
print('Is an Employee: ', isinstance(mgr_1, Employee))
print('Is an Developer: ', isinstance(mgr_1, Developer))

# issubclass() <-- Returns if a class is a Subclass to a parent class or not.
print('Is Manager sub class of Employee: ', issubclass(Manager, Employee))
print('Is Developer sub class of Employee: ', issubclass(Developer, Employee))
print('Is Developer Subclass of Manager: ', issubclass(Developer, Manager))

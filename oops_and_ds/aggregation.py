#
class Salary:     
  def __init__(self,pay,reward):    # creating a class object that takes two parameters pay and reward
    self.pay = pay
    self.reward = reward

  def annualized_sal(self):         # Creating a method that returns annualized salary
    return (self.pay*12)+self.reward


class Employee:   #
  def __init__(self,name,position,sal):
    self.name = name
    self.position = position
    self.final_sal = sal   #Instance object instead of a class object.

  def annual_salary(self):
    return self.final_sal.annualized_sal()    # Returning the method where in the final_sal became an instance object for the Salary Class Object

sal = Salary(90000,150000)

emp1 = Employee("Raj","Sr. Specialist",sal)    # Creating an instance Object

print(emp1.annual_salary())
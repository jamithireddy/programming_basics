#
class Salary:     # This is content
  def __init__(self,pay,reward):    # creating a class object that takes two parameters pay and reward
    self.pay = pay
    self.reward = reward

  def annualized_sal(self):         # Createing a method that returns annualized salary
    return (self.pay*12)+self.reward


class Employee:   # this is a container
  def __init__(self,name,posotion,pay,reward):
    self.name = name
    self.pay = pay
    self.final_sal = Salary(pay,reward)   #Initializing another class that can take the attributes pay and reward

  def annual_salary(self):
    return self.final_sal.annualized_sal()    # Returning the method where in the final_sal became an instance object for the Salary Class Object

emp1 = Employee("Raj","Sr. Specialist",90000,150000)    # Creating an instance Object

print(emp1.annual_salary())
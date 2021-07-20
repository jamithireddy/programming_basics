class Student:
  def  __init__(self):
      self.fname = 'Rajasekhar'
      self.lname = 'Jamithireddy'
      self.dob = '19850407'
      self.rollno = 3172
  
  def aboutme(self):
    print("Name - ",self.fname+ ' '+self.lname)
    print("Roll. Number - ",self.rollno)

s1=Student()
print(s1.fname)
s1.aboutme()

s1.fname="Lakshmi Prasanna"
s1.lname="Gulla"
s1.dob="19840702"
s1.rollno=2134
# While s1 shall show the updated values, s2 shall revert to the base template values
s1.aboutme()
s2=Student()
s2.aboutme()
# To access the memory location of the instance, we can use id
print(id(s1))
print(id(s2))
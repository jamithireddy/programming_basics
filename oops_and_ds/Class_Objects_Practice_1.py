
'''
TASK:

1. Take input from user (name,age,marks)

2. Create a class with __init__ method and also create a action method display() to print attributes

3. Also try to use Arguements and Parameters with diffrent objects
'''

# Creating input parameters

# n = input("Name: ")
# a = int(input("Age: "))
# m = int(input("Marks: "))

# Creating a Class
class Student:

  def __init__(self, n, a, **m): # Creating the constructor with the parameters and setting default values.
    self.name = n
    self.age = a
    self.marks = m

  def display(self):  # Creating a action method
    print('\n')
    print("Hi ", self.name)
    print("Your age is ", self.age)
    print("Your marks are ", self.marks)

# # Creating objects with the user inputs
# s1 = Student(n, a, m) # By default the first parameter is self and need not be mentioned

# # Calling a Action method

# s1.display()

# # Creating another object and passing in the values directly. We are skipping Marks as it has  a default value of zero.
# s2 = Student("Hima",30)
# s2.display()

#Entering Multiple values to the Mark as * was kept infront of m, it accepts as a tuple.

# s3 = Student("Rajasekhar",36,74,65,84,65,36)
# s3.display()

# By entering ** before m we have the keywords
s4 = Student("Naresh",34,Science=78,Maths=98,Social=74)
s4.display()
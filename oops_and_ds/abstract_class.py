# Normally we can create instance objects for the parent class as well as there is no restriction.
# Inorder to restrict creating instance objects from Parent class we use abstraction.
# Also the methods in parent class should be strictly implemented in child class.

from abc import ABC, abstractmethod

# import vs from:
# To conserve memory we import only certain specific classes

class Shape(ABC):   #We have made Shape class as abstract class 

  @abstractmethod   # By using'@abstractmethod' decorator, we made this method mandatory in any subsequent child classes.
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

class Square(Shape):
  def __init__(self,side):
    self.__side = side

  def area(self):
    return self.__side * self.__side

  def perimeter(self):    # If we try to omit perimeter or area, we get error as they were made abstract methods.
    return 4 * self.__side

square_obj =Square(10)

print(square_obj.area())



# Creating a class Polygon with private attributes
# We arent creating any object of Polygon class hence we havent called __init__
class Polygon:
  __width = None 
  __height = None

# since the attributes are private we need to  have get and set to update the values
  def set_value(self,width,height):
    self.__width = width 
    self.__height = height
  
  def get_width(self):
    return self.__width

  def get_height(self):
    return self.__height

# create a Square class and inherit all functionalities of Base class (Polygon) such as height, set_values, width, get_width and get_height
class Square(Polygon):
  def area(self):
    return self.get_width() * self.get_height()


# create a Triangle class and inherit all functionalities of Base class (Polygon) such as height, set_values, width, get_width and get_height
class Triangle(Polygon):
  def area(self):
    return 0.5 * self.get_width() * self.get_height()

s1=Square()
s1.set_value(8,15)
print(s1.area())

t1 =Triangle()
t1.set_value(5,10)
print(t1.area())
# Creating two classes named Polygon and color

class Polygon:
  __width = None 
  __height = None

  def set_values(self,w,h):
    self.__width = w
    self.__height = h
  
  def get_width(self):
    return self.__width

  def get_height(self):
    return self.__height

class Color:
  __color = None

  def set_color(self,col):
    self.__color = col

  def get_color(self):
    return self.__color
    
#Creating another class that inherits the classes Polygon and Color

class Square(Polygon,Color):
  def area(self):
    return self.get_width() * self.get_height()

  def color(self):
    return self.get_color()


class Triangle(Polygon,Color):
  def area(self):
    return self.get_width() * self.get_height() * 0.5

  def color(self):
    return self.get_color()

shape1 = Square()
shape1.set_values(8,15)
shape1.set_color("Blue")

shape2 =Triangle()
shape2.set_values(5,10)
shape2.set_color("Green")

print(shape1.area())
print(shape1.color())
print("---------------------")
print(shape2.area())
print(shape2.color())
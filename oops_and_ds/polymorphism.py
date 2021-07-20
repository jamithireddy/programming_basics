# To overwrite an operator to do special tasks, In this case we shall add pages of two books

class Books:
  def __init__(self,pages):
    self.pages=pages
    
  def __add__(self,other):
    return self.pages + other.pages

b1= Books(100)
b2 = Books(220)

print(b1+b2) #b1.__add__(b2)
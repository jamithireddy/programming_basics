class Parent1:
  def __init__(self,name):
    print("Parent1 init", name)

class Parent2:
  def __init__(self,name):
    print("Parent2 init", name)

class Child(Parent2,Parent1):   # The sequence mentioned here is imp as super picks the first mentioned
  def __init__(self):
    print("Child init")
    super().__init__("Rajasekhar")    # As Parent2 is mentioned first, it gets the Super()
    Parent1.__init__(self,"Hima")     # Without Super you have to declare the self too

child_obj = Child()
# Using Method resultion order to get what gets accessed first
print(Child.__mro__)
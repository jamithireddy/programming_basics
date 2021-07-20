# We can restrict access to methods and variables.This can prevent the data from being modified by accident and is known as encapsulation.


# Consdider the below example
class Speed:
    def __init__(self):
        self.speed = 10


s = Speed()
s.speed = 60
print(s.speed)

# In the above case we have modified the speed by just accessing outside the class.
print("_______________________________")
# In few cases this needs to be restricted. Hence we use private methods

# class Speed1:
#   def __init__(self):
#     self.__speed1 =10

# s =Speed1()
# #s.speed1 =60
# print(s.__speed1)
# # We get an error stating "AttributeError: 'Speed1' object has no attribute '__speed1'" as the attribute __speed1 is a private attribute.

# # A private member can be accessed only inside the class and creted by insering two underscores infront "__"
print("_____________")


class Speed2:
    def __init__(self):
        self.speed2 = 60
        self.__speed3 = 10


s2 = Speed2()
s2.speed2 = 80
print(s2.speed2)
s2.__speed3 = 100
print(s2.__speed3)

# We cannot access the private value but we can modify the value.


class Velocity:
    def __init__(self):
        self.velocity = 10
        self.__new_velocity = 80

    def get_new_velocity(self):
        return self.__new_velocity

    def set_new_velocity(self, new_vel):
        self.__new_velocity = new_vel


v = Velocity()
print(v.get_new_velocity())
v.set_new_velocity(100)
print(v.get_new_velocity())

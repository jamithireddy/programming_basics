result=None
x = int(input("Enter Number 1: "))
y = int(input("Enter Number 2: "))
try:
  result = x / y
except Exception as e:
  print("Error with our Code.",e,type(e))

print("Result = ",result)

class Tea:
  def __init__(self, temp):
    self.__temperature=temp

  def drink_tea(self):
    if self.__temperature >85:
      print("Hot to drink.")
    elif self.__temperature < 65:
      print("Cold to drink.")
    else:
      print("Ok to drink")

cup = Tea(100)
cup.drink_tea()

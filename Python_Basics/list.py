x = ["Rajasekhar ", 36, "Mechanical engineer", 'Python', 15.345]
len(x)

# Inserting a value in a particular Index
x.insert(1, "Jamithireddy")
print(x)

# consider a repeating value
y = ["ADB", "LHO", "SEETHAMMADHARA", "LHO",
     "AMALAPURAM", "LHO", "VIJAYANAGARAM"]

# <--- Removes the first  instance of the LHO .ie., one with the least index number
y.remove("LHO")
print(y)

y.pop()  # <-- removes the last element. i.e., the element with highest index number gets deleted
y.append("Reddipalle")  # <-- adds the element to the last place

# del vs clear

del x  # <-- Everything, even the variable name gets deleted.
y.clear()  # <-- This shall remove all the elements in y and makes it a empty list
# print(x) <-- We get name error trying to print this
print(y)


z = [4, 67, 45, 22, 90, 3, 16, 4]
z.sort()  # <-- Works with integers and floats. We get a sorted list
print(z)
z.reverse()  # <-- We get a reversed  list
print(z)
z.count(4)  # <-- Count gives How many times an element is present in the list

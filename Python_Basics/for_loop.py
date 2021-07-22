
A = [0, 1, 2, 3, 4, 5]   # List
B = (0, 1, 2, 3, 4, 5)  # Tuple
C = {0, 1, 2, 3, 4, 5}  # Set
D = "Rajasekhar"  # String
E = {"name": 'Rajasekhar', 'age': 36, 'designation': 'senior specialist',
     'company': 'deloitte'}  # Dictionary

print('s' in D)

for i in A:
    print(i, end='\t')

print('\n')
for i in D:
    print(i, end='\t')

# In case of a dictionary, For loop iterates over keys
print('\n')
for i in E:
    print(i, end='\t')

# Inorder to iterate over the values in a dictionary:
print('\n')
for i in E.values():
    print(i, end='\t')

# In order to go through both the key and Value pairs we need two variables
print('\n')
for i, j in E.items():
    print(i, '--->', j)

# Using Range
for x in range(0, 25, 5):
    print(x, end='\t')

# ! Break : Will stop the loop
# ! Continue : Skips that particular iteration from the loop

people = {'shankar': 'business man', 'hima': 'employee', 'raj': 'employee',
          'rekha': 'doctor', 'naresh': 'businessman', 'srujana': 'doctor', 'rajesh': 'banker'}
print('\n')
# print till we meet first doctor in the people

for i, j in people.items():
    if j != 'doctor':
        print(i.title(), 'is a', j.title())
    else:
        break

# Print all the people who arent doctors

print('-------------------------')

for i, j in people.items():
    if j != 'doctor':
        print(i.title(), 'is a', j.title())
    else:
        continue

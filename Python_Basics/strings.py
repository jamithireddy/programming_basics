x = "rajasekhar jamithireddy-rjamithireddy@gmail.com"

print(x.upper())

# Slicing the test based on Index

# first five characters for the string.index 0,1,2,3,4. However 5 is not included
print(x[0:5])

print(x[-5:])  # last five characters

y = "            akividu       , west Godavari          "

# STRIP Removes leading and trailing zeroes.
print("LSTRIP ----> ", y.lstrip())
print("RSTRIP ----> ", y.rstrip())
print("STRIP ----> ", y.strip())

# removing the double spaces and ' ,' in the text
print(y.replace("  ", "").replace(' ,', ','))

y = y.replace("  ", "").replace(' ,', ',').title()


# Splitting a string based on a character
check = x.find('-')
a = []
a.append(x[:check])
a.append(x[check+1:])
print(a)

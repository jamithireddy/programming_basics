# Setting the Basics for ethe out put command

x = 10
y = 20

print("The product of {0} and {1} is {2}".format(x, y, x*y))

myname = "Rajasekhar"

# Modulus method, commnly used in other laguage
print("My name is %s" % myname)

int_num = 1500
num = 123.444666

print("The two digit rounded float number is %.2f  and the intiger is %d" %
      (num, int_num))

# When we use , the space is automatically created. How ever the + doesnt create a space in the concatenation
print(" My name is", myname)
print("My name is"+myname)

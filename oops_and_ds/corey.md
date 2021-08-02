#### The goal of \_\_repr\_\_ is to be unambiguous <-- Meant for other coders.

#### The goal of \_\_str\_\_ is to be readable <-- Meant for end users.

> Suppose emp_1 is an instance of the class Employee which takes in first name, last name and pay. when we try and run the following code

```
repr(emp1)
```

We shall get the output as location on the memory map

```
<__main__.Employee object at 0x101b2b0f0>
```

When we include the the following block of code in the class Employee,

```
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.fname,self.lname,self.pay)
```

for _repr(emp1)_ we shall get the output as

```
Employee('Rajasekhar','Jamithireddy',90000)
```

This makes the code easy for a coder perspective to look at the inputs

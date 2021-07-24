# Object  oriented programming in Python

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0-100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # Though we havent passed this attribute as parameter, we can utilize it

    def add_student(self, student):
        if len(self.students) <= self.max_students:
            self.students.append(student)
            return True
        return False

    def get_avg_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 17, 65)
s4 = Student("James", 16, 84)

course = Course("Science", 2)

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
course.add_student(s4)
print(course.get_avg_grade())


#######################################################################################
#                                INHERETANCE                                         #
######################################################################################


class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print(" I dunno what I say!")

# Setting to inherit all the parameters, arguements and methods from the parent class Pet


class Cat(Pet):
    def speak(self):
        print("Meow")

# Suppose we need to mention the Dog's breed in the class as well, we shall have an __init__ with the dog class and then get the Parent class


class Dog(Pet):
    def __init__(self, name, age, breed):
        # self.name = name <-- We shall not be using these as we shall miss all the initializing done in the parent class
        # self.age= age    <-- We shall not be using these as we shall miss all the initializing done in the parent class
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("Bow wow")

    def show(self):
        print(f"I am {self.name}, I am a {self.age} year old {self.breed}")


p = Pet("Tim", 6)

p.show()
p.speak()     # The Parent class speak is default for all child classes. However when a method is specified in child class specifically, it gets overwritten
# Though there is no __init__ in Cat class the method show and the name and age parameters get inherited from the master
p1 = Cat("Chinnu", 3)
p2 = Dog("Roxy", 17, "Rotweiler")

p1.speak()
p1.show()

p2.speak()
p2.show()

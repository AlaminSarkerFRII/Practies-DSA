# What is __init__ in Python?

"""
The __init__ method in Python is a special 
method used for initializing newly created objects.
It’s called automatically when a new object of a class is created. This method can have arguments through which you can pass values for initializing object attributes.


"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p = Person("John", 30)
p.greet()  # Output: Hello, my name is John and I am 30 years old.
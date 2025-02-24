# Two main Topic in Polymorphism


# Function Overriding



class Parent:
    def display(self):
        print("Parent class display method")
        
        
        
class Child(Parent):
    def display(self):
        print("Child class display method")
        
        
        
        
c = Child() 

c.display() # Output - Child class display method




# Function Overloading


class Calculator:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c
    

c = Calculator()

c.add(1,2)
# Output - 3

c.add(1,2,3)
# Output - 6
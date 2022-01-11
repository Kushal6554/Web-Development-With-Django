# Class and objects
# Class is a user defined data type/structure
# Class contains data members and member functions
# Data members are variables that are part of the class, also called as attributes
# Member functions are functions that are part of the class, also called as methods

# Objects are instances of a class
# Objects can acess the data members and member functions of a class

# a single class can have multiple objects
# All the objects of a class share the same data members and member functions
# But the objects have differnt states, i.e., differnt values of data members

# Self is a reference variable that refers to the current instance of the class
# Class methods ust have self as the first argument


"""
class syntax
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-n>

object creation
objsct_name = ClassName()


"""

# Example
class Car:
    # Data members/attributes:
    a = "BMW"
    b = "Audi"
    c = "Mercedes"
    # Member functions/methods:
    def bmw(self):
        a1 = "Randomcar"
        print(f"Hello, I am a {self.a}!")

    def audi(self):
        print(f"Hello, I am a {self.b}!")

    def mercedes(self):
        print(f"Hello, I am a {self.c}!")

    def tesla(self):
        print(f"Hello, I am a tesla!")
    
obj1 = Car()
# obj2 = Car()
# obj3 = Car()

# c = obj1.bmw()
# print c
obj1.bmw() # Car.bmw(obj1)
obj1.a
obj1.audi()
obj1.mercedes()
obj1.tesla() # Car.tesla(obj1)

# print(obj1.a)
# obj1.hello()
# obj1.hello()
print(type(obj1))
# print(type(obj2))

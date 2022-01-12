# COnstructor, __init__, Class Variables, Instance Variables, __str__
# Constructor is a special method that is called when an object is created
# Is is used to initialize the state of the object

# Class variable is a variable that is shared by all the objects of a class
# Class variable is accessible by all the objects of the class
# Class variable is not a part of the object
# Class variable is also knnown as static variable

# Instance variables are variables whose value is assigned inside a constuctor or method with self
# Instance variabels are accessible by all the objects of the class.
# Instance variable is a part of the object
# Instance variable is not shared by all the objects of the class

# __str__ is a special method that is called upon when an objectis converted to a string.
# It is used to return a string representation of the object

class Vehicle:
    # Class Variable
    vehicle_type = "Car"

    # The init method or constructor
    def __init__(self, company):
        # Instance Variable
        self.company = company
    
    # Adds an instance variable
    def setColor(self, color): # def setColor(Obj1, "brown"):
        self.color = color #Obj1.color = "brown"

    # Retrieves instance variable
    def getColor(self): # def getColor(Obj1):
        return self.color # return Obj1.color

    def __str__(self):
        return f"This is a {self.company} {self.vehicle_type}"


Obj1 = Vehicle("BMW")
Obj1.setColor("Brown") # Vehicle.setColor(Obj1, "Brown")
print(Obj1.getColor()) # Vehicle.getColor(Obj1)
# Accessing class variable using class name
print(Vehicle.vehicle_type)
print(Obj1.getColor())

r = Obj1.__str__()
print(r)
print(type(r))

# Inheritance
# Inheritance is a way to create new classes based on existing classes.
# It is a way to reuse code.
# The inheritance is the capability of one class to derive or inherit the properties (data members/attributes/variables and methods) from another class.
# Parent class => Base class or Super class
# Child class => Sub class

# Example
class Person(object):
    def __init__(self, name):
        self.name = name
   
    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False

# Inherited or SUbclass (Note Person in bracket)

class Employee(Person):

    def isEmployee(self):
        return True

emp = Person("Bickky") # An object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Coursly") # An object of Employee
print(emp.getName(), emp.isEmployee())
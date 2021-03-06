# Inheritance: Constructor Overriding
# Constructor of the parent class is ovaailable in the child class
# But if we write constructor in both classes (parent and child class),  then the parent class constructor is not available to the child class
# In this case, only child class constructor is accessible which means child class consturctor is replacing the prent class constructor
# Calling constructor of the parent class in the child class is called constructor overriding
# Constructor with super() => is a function that s used to call the constructor of the parent class

# Example

# Parent class
class Person():
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# Child class
class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # Invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
        # or using super()
        # super().__init__(name, idnumber)

    def display2(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)

    def __str__(self):
        return f'{self.name} {self.idnumber} {self.salary} {self.post}'

# creation of an object varible or an instance
a = Employee('Kushal', '6554', '50K', 'Fullstack Developer')

# Calling a function of the class Person using its instance

a.display()
a.display2()
print(a.__str__()) # Kushal 6554 50K Fullstack Developer

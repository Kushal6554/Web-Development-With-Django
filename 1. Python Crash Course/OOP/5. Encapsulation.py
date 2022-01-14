# # Encapsulation
# # Public, private, protected access modifiers
# # Public: accessibel from anywhere
# # Protected: accessible only from inside the class and from its cubclasses.
# #   Also can be accessed from outside the class.
# #   However, it is a convention not to call protected methods from outside the class.
# # Private: accessible only from inside the class
# # Private: created using __ (two underscores) before the variable name
# # Protected: created using _ (one underscore) before the variable name

# class Student:
#     SchoolName = 'Birat Medical College'  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age  # Instance attribute


# std = Student("Kushal", 40)
# print(std.SchoolName)
# print(std.name)
# print(std.age)

# std.age = 39
# print(std.age)


# class Student:
#     _SchoolName = 'Birat Medical College'  # Protected class attribute

#     def __init__(self, name, age):
#         self._name = name  # Protected instance attribute
#         self._age = age  # Proteced instance attribute


# std = Student("Nilu", 35)
# print(std._SchoolName)
# print(std._name)
# print(std._age)
# std._age = 34
# print(std._age)


class Student:
    __SchoolName = "Karnali Academy of Health Sciences"  # Private class attribute

    def set(self, name, age):
        self.__name = name  # Private instance attribute
        self.__age = age    # Private instance attribute

    def __display(self):    # Private method
        print('This is private method.')

    def display2(self):
        print(self.__name)
        print(self.__age)


std = Student()
std.set("Kushal", 39)
print(std.display2())

# print(std.__SchoolName)
# print(std.__name)
# print(std.__Student__SchoolName)
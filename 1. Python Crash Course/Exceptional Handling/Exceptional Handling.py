# Exceptional Handling
# The try statement lets you test a block of code for errors
# The except statement lets you handle the error

'''
Differnt types of error are:
1. SyntaxError: When there is a syntactical error in Python code.
2. NameError: Raised when a variable is not found.
3. TypeError: Raises when a variable is use incorrectly.
4. ZeroDivisionError: Raised when the second operand of a division or modulo operation is zero.
5. IndexError: Raised when an index of a sequence is out of range.
6. KeyError: Raised when a key is not found in a dictionary.
7. AttributeError: Raised when an attribute that doesn't exist is accessed.
8. ModuleNotFoundError: Raised when a module is not found.
9. FileNotFoundError: Raised when a file is not found.
10. ValueError: Raised when a variable is assigned to a value that has an inappropriate type.
11. AssertionError: Raised when an asseet statement fails.
12. EOFError: Raised when the input() function hits an EOF.
13. KeyboardInterrupt: Raised when the user hits the interrupt key (normally Ctrl + C or Crtl + D) during input()
14. IndentationError: Raised when the Python code is not porperly indented.
15. TabError: Raised when the wrong number of tabs or spaces are used for indentation.
16. SystemError: Raised when the interpreter finds an internal problem, but cannot be specifically identified
17. SystemExit: Raised when Python interpreter is quit by calling the sys.exit() function.
18. Warning: Raised when the interpreter encounters a possible problem.
19. DeprecationWarning: Raised when the interpreter encounters a deprecated feature.
'''

'''
Syntax:
try:
    statement in try block
except:
    executed when error in try block
'''

# Example

try:
    a = 5
    b = 0
    print(a/b)
except:
    print('Some error has occurred')
print("Out of try/except blocks")

try:
    a = 5
    b = '0'
    print(a + b)
except TypeError:
    print("Unsupported Operation")
print("Out of try/except blocks")

try:
    a = 5
    b = 0
    print(a/b)
except TypeError:
    print("Unsupported Operation")
except ZeroDivisionError:
    print("Division by zero is not allowed")
print("Out of try/except blocks")

'''
try - except - else - finally
Syntax:
try:
    Statements in try block
except:
    Executed when error in try block
else:
    Executed when try block is error-free
finally:
    Executed irrespective of exeption occurred or not
'''

# Example
try:
    print("try block")
    x = int(input("Enter a number:\n"))
    y = int(input("Enter another number:\n"))
    z = x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print(f"Division by zero, ie, {y} is not accepted")
else:
    print("else block")
    print(f"{x} divided by {y} gives the result: {z}")
finally:
    print("finally block")
    x = 0
    y = 0
    print(f"Values of x and y are refreshed to x = {x} and y = {y}, respectively")
print("Out of try, except, else, and finally block")


# Raise an exception

try:
    x = int(input("Enter a number from 0 to 100:\n"))
    if x > 100 or x <0:
        raise ValueError(x)
except ValueError:
    print(f"{x} is out of the allowed range of numbers.")
else:
    print(f"{x} is within the allowed range of numbers")

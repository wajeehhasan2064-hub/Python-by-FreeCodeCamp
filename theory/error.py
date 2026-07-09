# Common Error Mistakes and Types -> to read error and correct code

#Syntax Error
# print("Hello, world!"
# SyntaxError: unexpected EOF in the end

#Name Error
# print(name)
# NameError: name 'name' is not defined

#Type Error
# 5 + "5"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

#Index Error
# my_list = [1, 2, 3]
# print(my_list[5])
# IndexError: list index out of range

#Attribute Error
# num = 42
# num.append(5)
# AttributeError: 'int' object has no attribute 'append'

# Debugging 

#You can debug by usinf print() and f function because it gives you more clarity of what to use and when
#You can debug by importing pdb module -> a bit complicated

import pdb
def divide(a, b):
    pdb.set_trace()
    return a / b
print(divide(10, 2))

#You can debug my making a breakpoint
#red dot on side of the number line

def divide(a, b):
    result = a / b
    return result
print(divide(10, 2))
print(divide(15, 3))

# Exception Handling
try: # -> try: The block of code where you anticipate an error might occur.
    x = 10 / 2
except ZeroDivisionError: # -> except: This block runs if an error of the specified type is raised inside the try block.
    print("You can't divide by zero!")
else: # -> else: Runs if no exception is raised in the try block.
    print('Division successful:', x)
finally: # -> finally: Runs no matter what, whether or not an exception occurred. Useful for clean-up tasks like closing files
    # or releasing resources.
    print('This block always runs.')

# Raise Statement
#Raise statement is a powerful tool that allows you to manually trigger exceptions in your code.It gives you control 
#over when and how errors are generated, enabling you to create custom error conditions and enforce specific program behavior.
def check_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')
    return age

try:
    check_age(-5)
except ValueError as e:
    print(f'Error: {e}') # Error: Age cannot be negative
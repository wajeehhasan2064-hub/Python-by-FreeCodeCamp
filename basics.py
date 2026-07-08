print("Hello World!")

#type() -> type function is used to determine the type of any function
developer = 'wajeeh'
print(type(developer))

#isinstance()
balance = 12
print(isinstance(balance, int))

# Python Standard Library

# math module has helpful functions for complex mathematical operations
# random module is helpful for generating random numbers
# re module is used for working with regular expressions
# datetime module is helpful for working with dates and times

# Import Statement -> to import modules

import math
import datetime

print(math.sqrt(36))

# To give small names to modules, you use as
# import math as m

# You can also call modules without import

from math import radians, sin, cos
angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value) # 0.6427876096865393
print(cos_value)  # 0.766044443118978

# To call every fucntion without specifying the name
from math import * # -> we use this
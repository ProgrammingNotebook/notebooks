# Modules in Python.

# 1. random

import random

dice = random.Random()
print(dice.randrange(1,7))

# 2. time

import time

print(time.process_time())

# 3. math

import math

print(math.pi)

#-------------------------------------------------------------------------------
# NOTE:
#   In order for you to create your own modules, you need to save your file with
# .py extension and all the methods and variable will be available in the file
# that imports it.
#-------------------------------------------------------------------------------

#-----------------------------
# 'import' statement variants
#-----------------------------

from math import cos, sin # Imports these functions directly

from math import *  # Import all the functions

import math as m
# Import math as m, so all functions can be accessed like m.pi instead of math.pi

from unit_tester import test

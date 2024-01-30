# randomly generate a number

import math as m  # aliasing as 'm'
import random

m.cos(m.pi)  # cos(pi)
m.factorial(5)  # factorial(5)

# common aliases:
# import numpy
# import scipy as sp
# import pandas as pd

# from math import pi
# from math import cos
# access w/o dot notation
# DANGEROUS! Avoid (unless you know what you're doing)
# from math import *  # wildcard '*'

# randomly generate a number with min and max adjustable
MIN = int(input("Enter min value: "))  # min value taken as an integer from the user
MAX = int(input("Enter max value: "))  # max value taken as an integer from the user
CORRECT = random.randint(MIN, MAX)  # returns a number between the min and max values

# until they guess correctly
while True:
    # prompt user for a guess
    GUESS = int(input(f"Pick a number between {MIN}-{MAX}: "))  # guess value taken as an integer from the user
    ATTEMPTS = 0  # default number of attempts taken to guess the number
    # compare that guess to correct number
    if GUESS < CORRECT:  # if guess value is less than correct value than print 'too low' and increase attempt
        # counter by 1
        print("Too low")
        ATTEMPTS = ATTEMPTS + 1  # if guess value is more than correct value than print 'too high' and increase
        # attempt counter by 1
    elif GUESS > CORRECT:
        print("Too high")
        ATTEMPTS = ATTEMPTS + 1
    # tell them high or low
    else:  # else break from loop
        break

# tell user correct number of guesses
print("You guessed", CORRECT, "in", ATTEMPTS, "attempts")

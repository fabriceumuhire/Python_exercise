"""
ODD NUMBERS FUNCTION
"""

NUMBER = 0
while NUMBER < 10:
    NUMBER += 1
    if NUMBER % 2 == 1:
        with open('odd_numbers.txt', 'a') as file:
            file.write(NUMBER)

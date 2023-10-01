import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
1. Prints a random number between 5-20
2. Prints a random number from the range 3 up to 10 but not including 10, with a step of 2, so it can print 3,5,7,9
3. Prints a random float number between 2.5 and 5.5 but does not include 5.5
"""

random_number = random.randint(1, 100)
print(random_number)

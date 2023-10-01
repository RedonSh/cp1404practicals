"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


"""
When will a ValueError occur? -if the user enters something that cannot be converted to an integer
When will a ZeroDivisionError occur? -if the user enters 0 as the denominato
Could you change the code to avoid the possibility of a ZeroDivisionError? -Yes, you can
"""
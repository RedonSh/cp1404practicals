user_name = input("Enter your name: ")

with open("name.txt", "w") as file:
    file.write(user_name)

with open("name.txt", "r") as file:
    user_name = file.read()

print(f"Your name is {user_name}")

with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())

result = num1 + num2
print("The sum of the first two numbers is:", result)

with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)

print("The total of all numbers in 'numbers.txt' is:", total)


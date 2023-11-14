import random

def main():
    user_score = float(input("Enter score: "))
    user_result = calculate_result(user_score)
    print(f"Result: {user_result}")

    random_score = random.randint(0, 100)
    random_result = calculate_result(random_score)
    print(f"Random Score: {random_score}, Result: {random_result}")
def calculate_result(score):
    if 0 <= score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"
    else:
        return "Invalid Input"

main()

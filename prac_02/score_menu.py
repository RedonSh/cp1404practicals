def get_valid_score():
    score = int(input("Enter a score (0-100 inclusive): "))
    while score < 100 or score > 0:
        if 0 <= score <= 100:
            return score
        else:
            print("Invalid input. Please enter a score between 0 and 100.")
            score = int(input("Enter a score (0-100 inclusive): "))

def print_result(score):
    print("The score is:", score)

def show_stars(score):
    print("*" * score)

while True:
    MENU = """(G)et a valid score 
(P)rint result
(S)how stars
(Q)uit"""

    print(MENU)
    choice = input("Pick one: ").upper()

    if choice == 'G':
        score = get_valid_score()
    elif choice == 'P':
            print_result(score)
    elif choice == 'S':
            show_stars(score)
    elif choice == 'Q':
        print("Farewell!")
        break
    else:
        print("Invalid input. Please select a valid option.")

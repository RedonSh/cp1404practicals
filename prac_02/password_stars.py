min_length = 8

def main():
    password = get_password()

    print('*' * len(password))


def get_password():
    password = input("Enter a password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long. Try again.")
        password = input("Enter a password: ")
    return password


main()
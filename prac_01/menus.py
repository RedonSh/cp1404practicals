

name = input("Enter name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice = input("choose one: ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid input")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input("choose one: ").upper()
print("Finished")


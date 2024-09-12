def intro():
    print("Welcome to the Adventure Travel Game!")

    print("You are embarking on a journey!!..")

    print("Your adventure begins now!!\n")


def start_game():
    print("You find yourself at a crossroad.")
    print("To your left is a dark forest.")
    print("To your right is an open field.")

    while True:
        choice = input("Which way do you want to go? Left or Right? ").lower()

        if choice == "left":
            print("\nYou chose to enter the dark forest.")
            forest()
            break
        elif choice == "right":
            print("\nYou chose to go to the open field.")
            field()
            break
        else:
            print("Invalid choice. Please enter 'left' or 'right'.\n")

def forest():
    print("\nYou are in the dark forest.")
    print("You hear strange noises around you.")
    print("Ahead of you, the path splits into two.")

    while True:
        choice = input("Do you want to go 'forward' or 'back'? ").lower()

        if choice == "forward":
            print("\nYou move deeper into the forest.")
            print("You encounter a wild animal!")
            print("You manage to scare it away and find a hidden treasure.")
            print("Congratulations! You found the treasure.\n")
            break
        elif choice == "back":
            print("\nYou decided to go back to the crossroad.")
            start_game()
            break
        else:
            print("Invalid choice. Please enter 'forward' or 'back'.\n")

def field():
    print("\nYou are in the open field.")
    print("You see a small town in the distance.")
    print("You also notice a cave nearby.")

    while True:
        choice = input("Do you want to go to the 'town' or 'cave'? ").lower()

        if choice == "town":
            print("\nYou head towards the town.")
            print("You find friendly villagers who offer you a place to rest.")
            print("You spend the night and continue your journey refreshed.\n")
            break
        elif choice == "cave":
            print("\nYou enter the dark cave.")
            print("It turns out to be a bear's den!")
            print("You barely manage to escape and run back to the crossroad.\n")
            start_game()
            break
        else:
            print("Invalid choice. Please enter 'town' or 'cave'.\n")

# Main game flow
intro()
start_game()
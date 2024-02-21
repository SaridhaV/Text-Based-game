import time

def intro():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(2)
    print("You find yourself standing in front of a mysterious cave.")
    time.sleep(2)
    print("Legend has it that inside the cave lies a great treasure.")
    time.sleep(2)
    print("Do you dare to enter?")

def choose_path():
    choice = input("Enter '1' to enter the cave or '2' to walk away: ")
    if choice == '1':
        cave()
    elif choice == '2':
        print("You decide not to enter the cave and walk away.")
        time.sleep(2)
        print("Game over.")
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        choose_path()

def cave():
    print("You cautiously enter the cave and find two tunnels.")
    time.sleep(2)
    print("One tunnel is dark and ominous, while the other is dimly lit.")
    time.sleep(2)
    print("Which tunnel do you choose?")
    time.sleep(2)
    tunnel_choice = input("Enter '1' for the dark tunnel or '2' for the lit tunnel: ")
    if tunnel_choice == '1':
        dark_tunnel()
    elif tunnel_choice == '2':
        lit_tunnel()
    else:
        print("Invalid choice. Please enter '1' or '2'.")
        cave()

def dark_tunnel():
    print("You enter the dark tunnel and hear eerie noises echoing around you.")
    time.sleep(2)
    print("Suddenly, you trip and fall into a pit, unable to escape.")
    time.sleep(2)
    print("Game over.")

def lit_tunnel():
    print("You cautiously make your way through the lit tunnel and find a chest.")
    time.sleep(2)
    print("You open the chest and discover it's filled with gold and jewels!")
    time.sleep(2)
    print("Congratulations! You've found the treasure.")
    time.sleep(2)
    print("You win!")

def main():
    intro()
    choose_path()

if __name__ == "__main__":
    main()
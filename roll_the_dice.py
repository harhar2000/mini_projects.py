# Write a program simulating rolling two dice. 
# Ask user if they want to roll the dice ('y' for yes, 'n' for no). 
# If 'y', generate and display two random numbers between 0 and 6.
# If 'n', display 'Thanks for playing' and exit. 
# For any other input, display 'Invalid choice!'.



import random

while True:
    choice = input("Roll the Dice?:  ").lower()
    if choice == "n":
        print("Thanks for playing")
        break
    elif choice == "y":
        die1 = random.randint(0,6)
        die2 = random.randint(0,6)
        print(f"({die1}, {die2})")
    elif choice != "y":
        print("Invalid choice!")

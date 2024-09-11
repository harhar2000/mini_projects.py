# Write a program generating a random number between 1 and 100. 
# The user is asked to guess the number. 
# If the guess is not a valid number, print an error message. 
# If the guess is too low, print "Too Low". 
# If the guess is too high, print "Too High".
# If the guess is correct, print "Congratulations! You guessed the number." 
# Keep asking for guesses until the correct number is guessed.


import random 


num = random.randint(1,100)
while True:
    try:
        choice = int(input("Guess the number between 1 and 100: "))
        if choice < num:
            print("Too Low")
        elif choice > num:
            print("Too High!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Enter a valid number")
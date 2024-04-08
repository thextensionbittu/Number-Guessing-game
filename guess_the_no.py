import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    while True:
        # Ask the player to guess the number
        user_guess = int(input("Enter your guess (between 1 and 100): "))
        
        # Check if the guess is correct
        if user_guess == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            break
        elif user_guess < number_to_guess:
            print("Try again. The number is higher.")
        else:
            print("Try again. The number is lower.")

# Run the game
number_guessing_game()

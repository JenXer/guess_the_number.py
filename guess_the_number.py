import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    while not guessed_correctly:
        # Get user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")

# Start the game
guess_the_number()

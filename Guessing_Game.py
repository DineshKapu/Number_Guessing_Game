import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Prompt the user to guess the number
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {attempts} attempts.")
            break
        # Provide feedback if the guess is too high
        elif guess > secret_number:
            print("Too high! Try again.")
        # Provide feedback if the guess is too low
        else:
            print("Too low! Try again.")

# Call the function to start the game
guess_number()
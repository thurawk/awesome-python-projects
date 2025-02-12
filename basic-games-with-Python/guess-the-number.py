import random
import time
import json

# Function to choose difficulty level
def select_difficulty():
    print("Choose your difficulty level:")
    print("1. Easy (1-50, 15 attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    difficulty = input("Enter your choice (1/2/3): ")

    if difficulty == "1":
        return random.randint(1, 50), 50, 15
    elif difficulty == "2":
        return random.randint(1, 100), 100, 10
    elif difficulty == "3":
        return random.randint(1, 200), 200, 5
    else:
        print("Invalid choice, defaulting to Medium.")
        return random.randint(1, 100), 100, 10

# Function to generate a hint based on the secret number
def give_hint(secret_number):
    if secret_number % 5 == 0:
        return "Hint: The number is divisible by 5!"
    elif secret_number % 3 == 0:
        return "Hint: The number is divisible by 3!"
    elif secret_number % 2 == 0:
        return "Hint: The number is divisible by 2!"
    else:
        return "Hint: The number is a prime number!"

# Function for the number guessing game
def number_guessing_game():
    # Select difficulty
    secret_number, upper_limit, max_attempts = select_difficulty()
    
    attempts = 0
    guesses = []
    start_time = time.time()

    # Read leaderboard
    try:
        with open("leaderboard.json", "r") as file:
            leaderboard = json.load(file)
    except FileNotFoundError:
        leaderboard = []

    # Game introduction
    print("\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and {upper_limit}.")
    print(f"You have {max_attempts} attempts to guess the number.\n")

    while attempts < max_attempts:
        try:
            # Get player guess
            guess = int(input("Enter your guess: "))
            attempts += 1
            guesses.append(guess)

            # Check guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                # Correct guess
                end_time = time.time()
                print(f"\nCongratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
                print(f"Time taken: {end_time - start_time:.2f} seconds.")

                # Save to leaderboard
                name = input("Enter your name for the leaderboard: ")
                leaderboard.append({"name": name, "attempts": attempts, "time": end_time - start_time})
                leaderboard.sort(key=lambda x: (x["attempts"], x["time"]))  # Sort by least attempts and time

                # Save updated leaderboard
                with open("leaderboard.json", "w") as file:
                    json.dump(leaderboard, file)

                break

            # Provide a hint after 5 attempts
            if attempts == 5:
                hint = give_hint(secret_number)
                print(hint)

        except ValueError:
            print("Please enter a valid integer.")

    if attempts == max_attempts and guess != secret_number:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.\n")

    # Display leaderboard
    print("\nLeaderboard:")
    for entry in leaderboard[:5]:  # Show top 5
        print(f"{entry['name']} - {entry['attempts']} attempts - {entry['time']:.2f} seconds")

    # Play again option
    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        number_guessing_game()

# Start the game
number_guessing_game()

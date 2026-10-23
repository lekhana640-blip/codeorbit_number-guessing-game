import random  # used to pick a random number

def get_valid_guess(low, high):
    """Keep asking until the user enters a valid whole number in range."""
    while True:
        try:
            guess = int(input(f"Enter your guess ({low}-{high}): "))
            if low <= guess <= high:
                return guess
            print(f"Please enter a number between {low} and {high}.")
        except ValueError:
            # Runs if the user types letters or leaves it blank
            print("Invalid input! Please enter a whole number.")

def play_round(low=1, high=100):
    """Play a single round and return the number of attempts taken."""
    secret = random.randint(low, high)  # random number for this round
    attempts = 0                        # counts guesses

    print(f"\nI'm thinking of a number between {low} and {high}.")

    while True:
        guess = get_valid_guess(low, high)
        attempts += 1

        if guess < secret:
            print("Too low! Try again.")
        elif guess > secret:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempt(s).")
            return attempts

def main():
    print("=== Number Guessing Game ===")
    rounds = 0
    best_score = None  # fewest attempts so far

    # Loop to allow multiple rounds
    while True:
        attempts = play_round()
        rounds += 1

        if best_score is None or attempts < best_score:
            best_score = attempts

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break

    print(f"\nThanks for playing! Rounds played: {rounds}")
    print(f"Your best score: {best_score} attempt(s)")

if __name__ == "__main__":
    main()
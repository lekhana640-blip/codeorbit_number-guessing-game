🎯 Number Guessing Game

A simple Python-based Number Guessing Game where the computer selects a random number and the player tries to guess it. The game provides hints after each guess and tracks the number of attempts taken to find the correct number.

📌 Features
*Generates a random number between 1 and 100
*Validates user input
*Provides hints:
  Too High
  Too Low
*Tracks the number of attempts
*Supports multiple rounds
*Records the best score (fewest attempts)

🛠️ Technologies Used
Python 3
Random module

▶️ How to Run
Install Python 3 on your system.
Download or clone this repository:
git clone https://github.com/your-username/number-guessing-game.git
Navigate to the project folder:
cd number-guessing-game
Run the program:
number_guessing_game.py

💻 Sample Output
=== Number Guessing Game ===

I'm thinking of a number between 1 and 100.

Enter your guess (1-100): 50
Too high! Try again.

Enter your guess (1-100): 25
Too low! Try again.

Enter your guess (1-100): 37
Correct! You guessed it in 3 attempt(s).

Play again? (y/n): n

Thanks for playing!
Rounds played: 1
Your best score: 3 attempt(s)

🔍 How It Works
The program generates a random number between 1 and 100.
The player enters a guess.
The game compares the guess with the secret number.
Hints are provided until the correct number is guessed.
The total number of attempts is displayed.
The player can choose to play additional rounds.

🎓 Learning Outcomes
This project helps in understanding:
*Python Functions
*Loops and Conditional Statements
*Exception Handling
*Input Validation
*Random Number Generation
*Basic Game Development Logic

🚀 Future Enhancements
Difficulty levels (Easy, Medium, Hard)
Scoreboard system
Timer-based challenges
Graphical User Interface (GUI)
Multiplayer mode

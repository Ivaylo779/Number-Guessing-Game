# Number Guessing Game

## Project Goals
The goal of this project is to create a fun and interactive number guessing game in Python.  
The Player tries to guess a randomly generated number within a certain range and has a limited number of tries.  
The game includes levels that increase the number range, making it harder and harder with every level.

## Solution
This game is implemented in Python using:
- **random** module for generating numbers
- **while loops** to manage gameplay
- **input validation** to handle user inputs safely
- **level system** that increases difficulty
- **try count** that limits the number of guesses per round

The game logic:
1. Generate a random number between 1 and the maximum (end).
2. The player has three chances to guess the number.
3. Give feedback if the guess is too high or too low.
4. Reveal the number if the player runs out of tries.
5. Offer options to advance to the next level, replay, or exit.

## Source Code
You can find the full source code here: [Number Guessing Game](https://github.com/Ivaylo779/Number-Guessing-Game/blob/master/number_guessing_game.py)

## Screenshots
### Level 1
![Level 1 Screenshot](https://github.com/Ivaylo779/Number-Guessing-Game/blob/master/Screenshot%202025-09-22%20144752.png)

### Level 2
![Level 2 Screenshot](https://github.com/Ivaylo779/Number-Guessing-Game/blob/master/Screenshot%202025-09-22%20144642.png)

### Game Over
![Game Over Screenshot](https://github.com/Ivaylo779/Number-Guessing-Game/blob/master/Screenshot%202025-09-22%20144410.png)

## Live Demo
You can try the game online: [Live Demo](https://replit.com/@ivaylobrezin/Number-Guessing-Game)

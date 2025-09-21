import random

computer_number = random.randint(1,100)

while True:
    player_input = input("Guess a number between 1 and 100: ")
    if not player_input.isdigit():
        print("Invalid input.Please,try again.")
        continue
    player_number = int(player_input)
    if player_number == computer_number:
        print("You guessed it!")
    elif player_number > computer_number:
        print("Too high!")
    else:
        print("Too low!")
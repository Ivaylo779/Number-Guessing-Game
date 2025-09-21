import random

computer_number = random.randint(1,100)

tries = 3
level = 0

while True:
    player_input = input("Guess a number between 1 and 100:")
    tries -= 1
    if not player_input.isdigit():
        print("Invalid input.Please,try again.")
        continue
    player_number = int(player_input)
    if player_number == computer_number:
        level += 1
        print(f"You guessed it!\nWould you like to advance to level {level}?")
        play_again = input("Yes/No")
        if play_again == "Yes":
            continue
        elif play_again == "No":
            break
        else:
            print("Invalid input,try again.")
    elif player_number > computer_number:
        print("Too high!")
    else:
        print("Too low!")
    if tries == 0:
        print("You ran out of tries!\nWould you like to play again?")
        play_again = input("Yes/No")
        if play_again == "Yes":
            continue
        elif play_again == "No":
            break
        else:
            print("Invalid input,try again.")
    else:
        print(f"You have {tries} tries left.")
import random

end = 100

computer_number = random.randint(1, end)

tries = 3
level = 1

while True:
    tries = 3
    player_input = input(f"Guess a number between 1 and {end}: ")
    tries -= 1
    if not player_input.isdigit():
        print("Invalid input. Please,try again.")
        continue
    player_number = int(player_input)
    if player_number == computer_number:
        print(f"You guessed it!\nWould you like to advance to level {level + 1}?")
        advance = input("Yes/No\n")
        if advance == "Yes":
            end += 100
            continue
        elif advance == "No":
            print(f"Would you like to play level {level} again?")
            play_again = input("Yes/No")
            if play_again == "Yes":
                continue
            elif play_again == "No":
                break
            else:
                print("Invalid input. Please,try again.")
        else:
            print("Invalid input. Please,try again.")
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
            print("Invalid input. Please,try again.")
    else:
        print(f"You have {tries} tries left.")
import random

stop = False
end = 100
level = 1

while True:
    computer_number = random.randint(1, end)
    print(f"----Level:{level}----")
    tries = 3
    while True:
        player_input = input(f"Guess a number between 1 and {end}: ")
        tries -= 1
        if not player_input.isdigit():
            print("Invalid input. Please,try again.")
            continue
        player_number = int(player_input)
        if player_number == computer_number:
            print(f"You guessed it!\nWould you like to advance to level {level + 1}?")
            advance = input("Yes/No\n").strip().lower()
            if advance == "yes":
                end += 100
                level += 1
                break
            elif advance == "no": 
                print(f"Would you like to play level {level} again?")
                play_again = input("Yes/No").strip().lower()
                if play_again == "yes":
                    break
                elif play_again == "no":
                    stop = True
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
            print(f"You ran out of tries!\nThe secret number was {computer_number}.\nWould you like to play again?")
            play_again = input("Yes/No").strip().lower()
            if play_again == "yes":
                break
            elif play_again == "no":
                stop = True
                break
            else:
                print("Invalid input. Please,try again.")
        else:
            print(f"You have {tries} tries left.")

    if stop:
        break
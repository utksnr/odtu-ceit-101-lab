import random

def game():
    u_win = 0
    c_win = 0
    draws = 0
    round = 0

    while round < 5:

        user_dice = random.randrange(7)
        computer_dice = random.randrange(7)

        if user_dice > computer_dice:
            u_win += 1
            print(f"User wins {user_dice} vs {computer_dice}")
            round += 1
        elif user_dice < computer_dice:
            c_win += 1
            print(f"Computer wins {user_dice} vs {computer_dice}")
            round += 1
        else:
            draws += 1
            print(f"Draw {user_dice} vs {computer_dice}")
            round += 1

    print("Reporting the results:")
    print("Total number of dice roll: 5.")
    print(f"The computer won {c_win} times.")
    print(f"The user won {u_win} times.")
    print(f"The drawn were {draws} times.")

while True:
    inputt =input("Press y to play rolling dice.")
    if inputt == "y":
        game()
    else:
        print("The game has ended.")
        break

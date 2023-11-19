import random

potion = 3
point = 0
sword = 3

print("You are in the middle of a maze.")

while True:
    print("Where to go?")
    x = input("Left[L], Right[R], Under[U], Down[D] ")

    if x not in ["L","R","U","D"]:
        print(f"Invalid way. Game ends. Point: {point}")
        break

    event = random.choice(["M","P","T","E"])

    if event == "M":
        print("A Monster!")
        if sword > 0:
            print("You fight the monster!")
            print("You saved yourself with a sword.")
            point += 1
            sword -=1
        else:
            print(f"You have no swords left. Monste Killed you. Game ends. Your points: {point}")

    elif event == "P":
        if potion >0:
            print("You drank a potion and saved yourself.")
            potion -=1
            point +=1
        else: 
            print(f"You have no potion left. You die. Game ends. Your points: {point}")
            break

    elif event == "T":
        print("You found a treasure and earned two points!")
        point +=2

    elif event == "E":
        print("Road is empty, Go ahaed!")
        point += 1

    print(f"Points: {point}")


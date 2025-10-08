name = input("What is your name? ")
print("Welcome", name, "to the adventures game")

answer = input("Your are infront of a blocked road where you can go to the left or to the right:")

if answer == "left":
    answer = input("You are about to enter a mysterious cave filled with hidden treasures. If you don’t wish to proceed, simply say 'Not Interested'(walk or Not Interested).")

    if answer == "walk":
        print("Welcome to my cave, Be ready to meet me!")

        answer1 = input("You are given with three option moving left, moving straight, moving right(left,straight,right); :")
        if answer1 == "left":
            print("You find the treaser, you can go out. You won the game🥳")
        elif answer1 == "straight":
            print("You are caught by the ghost, you lose the game. Better luck next time champ!😟")
        elif answer1 == "right":
            print("You can just walk out of the cave without the treaser 🙃")
    elif answer == "Not Interested":
        print("You are going to lose the game, Better luck next time!")
    else:
        print("Invalid option")

elif answer == "right":
    answer = input("You are going to enter a wild forest where you can walk around, run, and swim in the river(walk, run, cross, Not).")

    if answer == "walk":
        print("You will be attacked by a tiger, and you will lose the game. Better luck next time champ")
    elif answer == "run":
        print("You are being followed by a wide range of wild animals, and you must cross the gate to win the game.")
        answer2 = input("Do you want to cross or not?")
        if answer2 == "cross":
            print("You won the game, well played champ!. You got 10000 points🤩")
        else:
            answer2 == "Not"
            print("You lose the game, better luck next time champ!😟")
    elif answer == "swim":
        print("You are attacked by a shark and you lose the game, better luck next time champ!😟")
    else:
        print("Invalid option")
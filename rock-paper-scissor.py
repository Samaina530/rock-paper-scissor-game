
import random

playing = True
while playing:
    enter=input("Do you wanna play?(q to quit & y for yes) ")
    if enter=="q":
        break
    elif enter=="y":
        entry=input("Enter your choice (rock,paper,scissor): ")
        guesses = ["rock", "paper", "scissor"]
        r = random.choice(guesses)
        print(f'The computer has chosen {r}')

        if entry==r:
            print("It's a Draw!")
        elif entry=="paper" and r=="rock":
            print("It's a win!")
        elif entry=="scissor" and r=="paper":
            print("It's a win!")
        elif entry=="rock" and r=="scissor":
            print("It's a win!")
        else:
            print("You Lose!")
    else:
        print("Invalid Input")

input("Press Enter to close the game...")


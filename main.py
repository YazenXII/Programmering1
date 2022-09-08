comp_score = 0
user_score = 0

import random

while True:
    computer = random.choice(["rock", "paper", "scissors", "snake", "gun", "dragon", "sword", "luck", "lightning",])

    user = input("rock, paper or scissors? ")

    print("The computer chose", computer,"and the user chose", user +".")

    if computer == ("rock") and user == ("paper"):
        print("one point goes to you.")
        score += 1

    if computer == ("paper") and user == ("rock"):
        print("one point goes to the computer.")

    if computer == ("scissors") and user == ("rock"):
        print("one point goes to you.")

    if computer == ("rock") and user == ("scissors"):
        print("one point goes to the computer")

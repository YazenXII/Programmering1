import random


user_cash = int(input("How much cash do you possess?"))
while not (bet := input("How much do you wish to sacrifice?")).isdigit():
    print("Insert Error, please write only in digits.")
bet = int(bet)
user_cash -= bet
print(
    "your current balance has been updated too",
    user_cash,
    "Dollars, thank you for your purchase. You may enjoy yourself.",
)

Royalty = "Jack", "Queen", "King"

dealer_cards = []
player_cards = []
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "jacks", "queen", "king"]

while True:
    action = input(
        "1. gaze cards\n" "2. Hit\n" "3. Stand\n" "4. Double\n" "5. Split\n" "6. Exit\n"
    )

    if action == "1":
        print(player_cards)

    if action == "2":
        random.shuffle = cards
        player_cards.pop()
        print(player_cards)
    if action == "6":
        break

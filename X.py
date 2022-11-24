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
"""
while not (money := input()).isdigit():
    print("Please insert an amount.")

dealer_cards = []
player_cards = []
cards = int(2, 3, 4, 5, 6, 7, 8, 9, "jacks", "queen", "king").capitalize()

while True:
    cards = input("1. gaze cards\n" "2. Hit\n" "3. Stand\n" "4. Double\n" "5. Split\n")
"""

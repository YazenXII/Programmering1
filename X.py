import random

# beting system


def sum_of_cards(local_list=list):
    sum_of_cards = 0
    for item in local_list:
        if item.isnumeric():
            sum_of_cards += int(item)
        else:
            sum_of_cards += 10
    return sum_of_cards


while True:
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
    # dem här ska vara värd 10

    # Deck

    Royalty = ["Jacks", "Queen", "king"]
    dealer_cards = []
    player_cards = []
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jacks", "Queen", "king"]

    def dealer_sum():

        for card in dealer_cards:
            dealer_sum = 0
        if cards in Royalty:
            dealer_sum += 10

    for card in player_cards:
        player_sum = 0
    if cards in Royalty:
        player_sum += 10

    # Hur båda får deras kort

    for i in range(2):
        random.shuffle(cards)
        uttaget_kort = cards.pop()
        player_cards.append(uttaget_kort)

    for i in range(2):
        random.shuffle(cards)
        uttaget_kort = cards.pop()
        dealer_cards.append(uttaget_kort)

    # olika val man har

    while True:
        action = input(
            "1. gaze cards\n"
            "2. Hit\n"
            "3. Stand\n"
            "4. Double\n"
            "5. Split\n"
            "6. Exit\n"
        )

        # för att se dina och dealers kort

        if action == "1":
            print("your cards", player_cards)
            print("dealer cards", dealer_cards)

        # Att få ett till kort

        if action == "2":
            random.shuffle(cards)
            shuffle_cards = cards.pop()
            player_cards.append(shuffle_cards)
            print(player_cards)
        if sum_of_cards(dealer_cards) >= 21:
            print("Bust")

        # Det innebär att spelaren har slutat sin tur och dealer ska spela nu

        if action == "3":
            while True:
                random.shuffle(cards)
                shuffle_cards = cards.pop()
                dealer_cards.append(shuffle_cards)

                if sum_of_cards(dealer_cards) >= 17:
                    print(dealer_cards)
                    break

                if sum_of_cards(dealer_cards) > 21:
                    print(dealer_cards)
                    print("The dealer has gone over 21, player wins")
                    break

                if sum_of_cards(player_cards) > sum_of_cards(dealer_cards):
                    print("player wins")

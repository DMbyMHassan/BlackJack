 #black project 2023  CNA
import random
from decimal import Decimal
import db

MIN_BET = 5
MAXIMUM_BIT = 100
BLACKJACK_PAY = Decimal('1.5')

def get_bet_amount(money):
    while True:
        try:
            bet_amount = Decimal(input(f"Money: {money}\nBet Amount: "))
            if bet_amount < MIN_BET or bet_amount > MAXIMUM_BIT:
                print(f"Invalid bet amount. Please enter a bet between {MIN_BET} and {MAXIMUM_BIT}.")
            elif bet_amount > money:
                print("You don't have enough money to place that bet.")
            else:
                return bet_amount
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_card_value(card):
    return [2]

def get_hand_points():
    pass
def print_cards_dealer():
    pass
def print_cards_palyer():
    pass



def main():
    print("BLACKJACK")
    print("Blackjack payout 3:2")
    money = db.read_money()
    while money > 0:
        db.write_money(money)
        bet_amount = get_bet_amount(money)
        random.shuffle(deck)





if __name__ == '__main__':
    main()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

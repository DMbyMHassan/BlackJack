# black project 2023  CNA Mahmoud Hassan
import decimal
import random
from decimal import Decimal
import db
import card
import sys

# definig the min and max bit as global vriable and Blackjack pay
MIN_BET = 5
MAXIMUM_BIT = 100
BLACKJACK_PAY = Decimal('1.5')


# get bet amount and vlaidate to be between minmum and maximum range
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
        except decimal.InvalidOperation:
            print("Invalid input. Please enter a number.")
        except Exception:
            print("An unexcpected error occured")
            sys.exit()


# This function returns the point value of a card
def get_card_value(card):
    return card[2]


# This function to calculate hand points
def get_hand_points(hand):
    points = sum(get_card_value(card) for card in hand)
    sum_aces = sum(1 for card in hand if card[1] == 'Ace')
    while points > 21 and sum_aces > 0:
        points -= 10
        sum_aces -= 1
    return points


# printing the Dealer cards
def print_cards_dealer(cards, hidden_card=False):
    print()
    if hidden_card:
        print("DEALER' SHOW CARD:")
        print(f"{cards[1][1]} of {cards[1][0]}")
    else:
        print("DEALER'S CARDS:")
        for card in cards:
            print(f"{card[1]} of {card[0]}")


# printing the player cards
def print_cards_palyer(cards):
    print("\nYOUR CARDS:")
    for card in cards:
        print(f"{card[1]} of {card[0]}")


def main():
    print("BLACKJACK")
    print("Blackjack payout 3:2")

    # read money from file
    money = db.read_money()

    while money > MIN_BET:
        db.write_money(money)
        bet_amount = get_bet_amount(money)

        # creat new shuffled deck
        deck = card.create_deck()
        random.shuffle(deck)

        # Deal two card for everyone
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # showing card with face down for one card for the dealar
        print_cards_dealer(dealer_hand, hidden_card=True)

        # show the player,s cards
        print_cards_palyer(player_hand)

        # calculte points for every one
        player_points = get_hand_points(player_hand)
        dealer_points = get_hand_points(dealer_hand)

        # check if the player have black jack
        if player_points == 21:
            print(f"Your points: {player_points} Dealer Points :{dealer_points}")
            print("BLACKJACK")
            money += bet_amount.quantize(Decimal('0.01')) * BLACKJACK_PAY
        else:
            while True:
                respons = input("Hit or stand? (hit/stand)")
                if respons.lower() == 'hit':
                    player_hand.append(deck.pop())
                    print_cards_palyer(player_hand)
                    player_points = get_hand_points(player_hand)


                    # check if the player busted
                    if player_points > 21:
                        print(f"Your points: {player_points} Dealer Points :{dealer_points}")
                        print("Sorry you lose!")
                        money -= bet_amount
                        break
                elif respons.lower() == 'stand':
                    print_cards_dealer(dealer_hand)
                    while dealer_points < 17:
                        dealer_hand.append(deck.pop())
                        dealer_points = get_hand_points(dealer_hand)
                        print_cards_dealer(dealer_hand)
                    # check if delear busted
                    if dealer_points > 21:
                        print(f"Your points: {player_points} Dealer Points :{dealer_points}")
                        print("DEALER BUSTS!")
                        money += bet_amount
                    elif dealer_points > player_points:
                        print(f"Your points: {player_points} Dealer Points :{dealer_points}")
                        print("DEALER WINS!")
                        money -= bet_amount
                    elif dealer_points < player_points:
                        print(f"Your points: {player_points} Dealer Points :{dealer_points}")
                        print("BLACKJACK!")
                        print("YOU WIN!")
                        money += bet_amount
                    break
                else:
                    print("Invalid input. please enter hit or stand")
    # giving option for the player to buy more chips and play again
    while money <= MIN_BET:
        print("You donot have enough money")
        respons = input("Would you like to buy more chips (y/n): ")
        while respons.lower() == 'y':
            money += Decimal(input(f"How many chips would like to buy: "))
            while money < 5:
                money += Decimal(input(f"Add More Money ,AS Minum bit is 5; how much would like to add more?"))
            db.write_money(money)
            bet_amount = get_bet_amount(money)
            deck = card.create_deck()
            random.shuffle(deck)
            player_hand = [deck.pop(), deck.pop()]
            dealer_hand = [deck.pop(), deck.pop()]
            print_cards_dealer(dealer_hand, hidden_card=True)
            print_cards_palyer(player_hand)
            player_points = get_hand_points(player_hand)
            dealer_points = get_hand_points(dealer_hand)
            if player_points == 21:
                print(f"Your points: {player_points} Dealer Points :{dealer_points}")
                print("BLACKJACK")
                money += bet_amount.quantize(Decimal('0.1')) * BLACKJACK_PAY
            else:
                while True:
                    respons = input("Hit or stand? (hit/stand): ")
                    if respons.lower() == 'hit':
                        player_hand.append(deck.pop())
                        print_cards_palyer(player_hand)
                        player_points = get_hand_points(player_hand)
                        if player_points > 21:
                            print(f"Your points: {player_points} Dealer Points :{dealer_points}")
                            print("looser!")
                            money -= bet_amount
                            break
                    elif respons.lower() == 'stand':
                        print_cards_dealer(dealer_hand)
                        while dealer_points < 17:
                            dealer_hand.append(deck.pop())
                            dealer_points = get_hand_points(dealer_hand)
                            print_cards_dealer(dealer_hand)
                        if dealer_points > 21:
                            print(f"Your points: {player_points} Dealer Points :{dealer_points}")
                            print("DEALER BUSTS!")
                            money += bet_amount
                        elif dealer_points > player_points:
                            print(f"Your points: {player_points} Dealer Points :{dealer_points}")
                            print("DEALER WINS!")
                            money -= bet_amount
                        elif dealer_points < player_points:
                            print(f"Your points: {player_points} Dealer Points :{dealer_points}")
                            print("BLACKJACK!")
                            print("YOU WIN!")
                            money += bet_amount
                        break
                    else:
                        print("Invalid input. please enter hit or stand")
        else:
            print("Good luck next time")
            break


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

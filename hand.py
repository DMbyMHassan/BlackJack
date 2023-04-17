# This module to  calculates value of the hand , and including A"ces" that can be valued as 1 or 11

def get_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        card_value = card.get_card_value(card)
        if card_value == 11:
            aces += 1
        value += card_value
    while aces > 0 and value > 21:
        value -= 10
        aces -= 1
    return value


# Displays the given hand

def display_hand(hand):
    for card in hand:
        print(f'{card[0]} of {card[1]}')

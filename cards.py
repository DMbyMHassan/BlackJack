# this module to define deck cards using list to store suits,rank and points

import random

SUITS = ['Hearts','Diamonds','clubs', 'Speades']
RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
VALUE = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
         'Queen': 10, 'King': 10}

def creat_deck():
    pass

def shuffle_deck():
    random.shuffle()
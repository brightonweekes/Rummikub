import random


# Define the Tile class and give it color and value attributes
class Tile:
    def __init__(self, color, value):
        self.color = color
        self.value = value


# Define the deck and fill it with appropiate tiles
deck = []

for i in range(2):
    for i in range(4):
        for j in range(13):
            deck.append(Tile(color=i+1, value=j+1))

    deck.append(Tile(color=0, value=0))     # Joker tiles

random.shuffle(deck)


# Define the Player class and assign draw and hand sort functions
class Player:
    def __init__(self, hand):
        self.hand = hand

    def draw_tile(self):
        self.hand.append(deck[0])
        deck[0].remove()
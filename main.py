import random
import pygame


# Define the Tile class and give it color and value attributes
class Tile:
    def __init__(self, color, value):
        self.color = color
        self.value = value
        on_board = False


# Define the deck and fill it with appropiate tiles
deck = []

for i in range(2):
    for i in range(4):
        for j in range(13):
            deck.append(Tile(color=i+1, value=j+1))

    deck.append(Tile(color=0, value=0))     # Joker tiles

random.shuffle(deck)

# Define other variables
fps = 60
backdrop_color = '#325320'
player_count = 2
starting_tile_count = 14


# Define the Player class and assign functions
class Player:
    def __init__(self):
        self.hand = []
        self.has_placed = False     # Store whether the player has placed their initial sets adding to 30 or greater

    def draw(self):
        self.hand.append(deck[0])
        deck.pop(0)

    def place(self):
        pass


# Main game turn logic
def main():
    pass


# Backend setup
board = []      # List containing all lists of tiles on board
players = []    # List containing all Player objects
for player in range(player_count):
    players.append(Player())
    for starting_tile in range(starting_tile_count):
        players[player].draw()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(backdrop_color)

    # RENDER YOUR GAME HERE
    main()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(fps)  # limits FPS to 60

pygame.quit()

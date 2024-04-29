import random
import os
import pygame

# Define global variables
fps = 60
backdrop_color = '#325320'
player_count = 2
current_player = 0
starting_tile_count = 14
screen_resolution = screen_width, screen_height = 1600, 900
title = 'Rummikub'


# Define the Tile class and give it color and value attributes
class Tile:
    def __init__(self, color, value):
        self.color = color
        self.value = value
        on_board = False


# Define the Player class and assign functions
class Player:
    def __init__(self):
        self.hand = []
        self.hand_backup = []
        self.has_placed = False     # Store whether the player has placed their initial sets adding to 30 or greater

    def draw(self):
        self.hand.append(deck[0])
        deck.pop(0)

    def place(self):
        pass


# Main game turn logic
def main():
    pass
    

# Check if current board state is correct
def check_board():
    valid_board = False

    return valid_board


def pass_turn():
    global current_player
    current_player = (current_player+1) % player_count


# Define the deck and fill it with appropiate tiles
deck = []

for i in range(2):
    for i in range(4):
        for j in range(13):
            deck.append(Tile(color=i+1, value=j+1))

    deck.append(Tile(color=0, value=0))     # Joker tiles

random.shuffle(deck)

# Backend setup
board = []              # List containing all lists of tiles on board
board_backup = []       # Stores board as it was in beginning of turn
ui_board = []           # Stores coordinate locations for each tile displayed on the board
ui_board_backup = []    # Stores ui board as it was in beginning of turn
players = []            # List containing all Player objects
for player in range(player_count):
    players.append(Player())
    for starting_tile in range(starting_tile_count):
        players[player].draw()



# pygame setup
pygame.init()
screen = pygame.display.set_mode(screen_resolution)
clock = pygame.time.Clock()

# Load UI Elements
tile_holder = pygame.image.load('uiImages/tile_holder.jpg').convert_alpha()
tile_holder = pygame.transform.scale(tile_holder, (screen_width*.9, screen_height*.15))
tile_rect = tile_holder.get_rect(midbottom = (screen_width/2, screen_height))

joker_icon = pygame.image.load('uiImages/joker_face.png').convert_alpha()

done_image = pygame.image.load('uiImages/done.png').convert_alpha()
done_image = pygame.transform.smoothscale_by(done_image, .33)
done_rect = done_image.get_rect(center = (screen_width-100, screen_height-300))

undo_image = pygame.image.load('uiImages/undo_image.jpg').convert_alpha()
undo_rect = undo_image.get_rect(center = (screen_width-100, screen_height-500))

pygame.display.set_caption(title)
pygame.display.set_icon(joker_icon)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(backdrop_color)
    screen.blit(tile_holder, tile_rect)
    screen.blit(done_image, done_rect)
    screen.blit(undo_image, undo_rect)



    main()

    pygame.display.update()

    clock.tick(fps)

pygame.quit()

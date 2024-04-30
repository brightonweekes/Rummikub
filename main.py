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


# Define the Player class and assign functions
class Player:
    def __init__(self):
        self.hand = []
        self.hand_backup = []
        self.has_placed = False     # Store whether the player has placed their initial sets adding to 30 or greater

    def draw(self):
        self.hand.append(deck[0])
        deck.pop(0)


# Passes turn to next player
def pass_turn():
    global current_player
    current_player = (current_player+1) % player_count


# Determines how a tile should look and draws it to screen
def render_tile(tile):
    global tile_grid
    if tile[2] == 0:
        tile[0].fill('#325320')
    elif tile[2] == 1:
        tile[0].fill('#1E5E1C')
    else:
        tile[0].fill('black')
    screen.blit(tile[0], tile[1])


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

# Creates a global grid on whch all tiles will be placed
tile_grid = []
for row in range(9):
    tile_grid.append([])
    for pos in range(15):
        tile_grid[row].append([pygame.Surface((100, 100)), pygame.Rect(pos*100, row*100, 100, 100), 0])     # Each grid tile has a surface, a Rect for storing location, 
                                                                                                            #and a value which determines what is displayed

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
done_image = pygame.transform.smoothscale_by(done_image, .20)
done_rect = done_image.get_rect(center = (screen_width-50, screen_height-300))

tile_images = [[], [], [], []]

for image in os.listdir('uiImages/'):
    if image[0].isdigit():
        tile_images[int(image[0])-1].append(pygame.image.load(f'uiImages/{image}').convert_alpha())

for color in range(len(tile_images)):
    for tile in range(len(tile_images[color])):
        tile_images[color][tile] = pygame.transform.smoothscale_by(tile_images[color][tile], .10)

# Set tite and caption
pygame.display.set_caption(title)
pygame.display.set_icon(joker_icon)

# Main loop
running = True

while running:                   

    screen.fill(backdrop_color) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for tile_row in enumerate(tile_grid):
        for tile_pos in enumerate(tile_row[1]):
            if tile_pos[1][1].collidepoint(pygame.mouse.get_pos()):
                # print('collided with rectangle starting at '+str(tile_pos[1][1].left)+str(tile_pos[1][1].top))
                tile_pos[1][2] = 1
            else:
                tile_pos[1][2] = 0
            render_tile(tile_pos[1])

    screen.blit(tile_holder, tile_rect)
    screen.blit(done_image, done_rect)


    for tile in players[player].hand:
        screen.blit(tile_images[tile.color-1][tile.value-1], (0, 0))


    pygame.display.update()

    clock.tick(fps)

pygame.quit()

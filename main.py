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
        self.has_placed = False     # Store whether the player has placed their initial sets adding to 30 or greater

    def draw(self):
        self.hand.append(deck[0])
        deck.pop(0)


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

# Creates a global grid on whch all tiles will be placed
tile_grid = []
for row in range(9):
    tile_grid.append([])
    for pos in range(15):
        tile_grid[row].append([pygame.Surface((100, 100)), pygame.Rect(pos*100, row*100, 100, 100), None])     # Each grid tile has a surface, a Rect for storing location

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
tile_rect = tile_holder.get_rect(bottomleft = (30, 880))

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

main_font = pygame.font.Font(None, 50)
current_player_surface = main_font.render(str(current_player), True, 'black').convert_alpha()
current_player_rect = current_player_surface.get_rect(topright = (1580, 100))

# Set tite and caption
pygame.display.set_caption(title)
pygame.display.set_icon(joker_icon)

# Main loop
running = True

while running:                   

    tile_has_placed = False
    screen.fill(backdrop_color) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if done_rect.collidepoint(event.pos):                       # If the continue button is pressed
                if tile_has_placed:
                    pass
                # check board state to see if its valid
                else:
                    players[current_player].draw()
                
                    current_player = (current_player+1) % player_count      # Pass to next player
                    current_player_surface = main_font.render(str(current_player), True, 'black').convert_alpha()

            for tile_row in tile_grid:
                for tile_pos in tile_row:
                    if tile_pos[1].collidepoint(event.pos):
                        if tile_pos[2] != None:
                            pass







    for tile_row in enumerate(tile_grid):
        for tile_pos in enumerate(tile_row[1]):
            if tile_pos[1][1].collidepoint(pygame.mouse.get_pos()):
                tile_pos[1][0].fill('#1E5E1C')
            else:
                tile_pos[1][0].fill('#325320')
            screen.blit(tile_pos[1][0], tile_pos[1][1])

    screen.blit(tile_holder, tile_rect)
    screen.blit(done_image, done_rect)
    screen.blit(current_player_surface, current_player_rect)


    for tile in enumerate(players[current_player].hand):
        screen.blit(tile_images[tile[1].color-1][tile[1].value-1], (tile[0]%15*100, 800 - tile[0]//15*100))     # Draws each tile in player hand at correct location
        for row in tile_grid:
            for pos in row:
                if pos[1].collidepoint((tile[0]%15*100, 800 - tile[0]//15*100)):
                    pos[2] = tile[1]        # Stores what tile is at each location in the tile_grid


    pygame.display.update()

    clock.tick(fps)

pygame.quit()

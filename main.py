import random
import pygame

# Define global variables
fps = 60
backdrop_color = '#325320'
player_count = 2
current_player = 0
starting_tile_count = 14
display_resolution = (screen_width, screen_height) = (1600, 900)


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


def resize_screen():
    global tile_holder
    tile_holder = pygame.transform.scale(tile_holder, (screen_width*.8, screen_height*.15))


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

# Load UI Elements
tile_holder = pygame.image.load('./uiImages/tile_holder.png')
# done button



resize_screen()

# pygame setup
pygame.init()
screen = pygame.display.set_mode(display_resolution)
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(backdrop_color)
    screen.blit(tile_holder, (screen_width/2-tile_holder.get_width()/2, screen_height-tile_holder.get_height()))

    main()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(fps)  # limits FPS to 60

pygame.quit()

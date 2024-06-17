import pygame as pg
import sys
import time
from pygame.locals import *

# Initialize Pygame
pg.init()

# Set up the window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
LINE_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = WHITE

# Set up the game board
BOARD_SIZE = 3
CELL_SIZE = WINDOW_WIDTH // BOARD_SIZE

# Set up the players
X = "X"
O = "O"

# Function to draw the grid lines
def draw_grid(surface):
    for i in range(1, BOARD_SIZE):
        # Vertical lines
        pg.draw.line(surface, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_HEIGHT), 2)
        # Horizontal lines
        pg.draw.line(surface, LINE_COLOR, (0, i * CELL_SIZE), (WINDOW_WIDTH, i * CELL_SIZE), 2)

# Function to draw X's and O's
def draw_xo(surface, board, x_image, o_image):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == X:
                surface.blit(x_image, (col * CELL_SIZE + 10, row * CELL_SIZE + 10))
            elif board[row][col] == O:
                surface.blit(o_image, (col * CELL_SIZE + 10, row * CELL_SIZE + 10))

# Function to check for win
def check_win(board, player):
    # Check rows and columns
    for i in range(BOARD_SIZE):
        if all(board[i][j] == player for j in range(BOARD_SIZE)):
            return True
        if all(board[j][i] == player for j in range(BOARD_SIZE)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True
    if all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True
    return False

# Function to check for draw
def check_draw(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

# Function to reset the board
def reset_board():
    return [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Load images
x_image = pg.image.load("x.png")
o_image = pg.image.load("o.png")

# Resize images
x_image = pg.transform.scale(x_image, (CELL_SIZE - 20, CELL_SIZE - 20))
o_image = pg.transform.scale(o_image, (CELL_SIZE - 20, CELL_SIZE - 20))

# Set up the window
WINDOW = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Tic Tac Toe")

cover_image = pg.image.load("cover.png")
cover_image = pg.transform.scale(cover_image, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Set up the game variables
current_player = X
board = reset_board()
game_over = False
winner = None

# Display the cover image for 3 seconds
start_time = time.time()
while time.time() - start_time < 3:
    WINDOW.blit(cover_image, (0, 0))
    pg.display.update()

# Main game loop
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        if not game_over and event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y // CELL_SIZE
            col = x // CELL_SIZE
            if board[row][col] == "":
                board[row][col] = current_player
                if check_win(board, current_player):
                    winner = current_player
                    game_over = True
                elif check_draw(board):
                    game_over = True
                current_player = O if current_player == X else X
    # Fill the background color
    WINDOW.fill(BACKGROUND_COLOR)
    # Draw the grid
    draw_grid(WINDOW)
    # Draw X's and O's
    draw_xo(WINDOW, board, x_image, o_image)
    # Display winner or draw message
    if game_over:
        font = pg.font.Font(None, 150)
        if winner:
            WINDOW.fill(BACKGROUND_COLOR)
            text = font.render(f"{winner} wins!", True, (0, 0, 255))
        else:
            WINDOW.fill(BACKGROUND_COLOR)
            text = font.render("Draw!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        WINDOW.blit(text, text_rect)
    pg.display.update()
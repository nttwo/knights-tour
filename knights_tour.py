import pygame
import sys
import time

# Knight's move directions
MOVE_X = [2, 1, -1, -2, -2, -1, 1, 2]
MOVE_Y = [1, 2, 2, 1, -1, -2, -2, -1]

BOARD_SIZE = 8
SQUARE_SIZE = 80
WIDTH = HEIGHT = BOARD_SIZE * SQUARE_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (211, 211, 211)
BLUE = (30, 144, 255)
FONT_SIZE = 24
DELAY = 0.2  # seconds

def is_valid_move(x, y, board):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and board[y][x] == -1

def count_onward_moves(x, y, board):
    count = 0
    for i in range(8):
        nx, ny = x + MOVE_X[i], y + MOVE_Y[i]
        if is_valid_move(nx, ny, board):
            count += 1
    return count

def next_move(x, y, board):
    min_deg_idx = -1
    min_deg = 9
    for i in range(8):
        nx, ny = x + MOVE_X[i], y + MOVE_Y[i]
        if is_valid_move(nx, ny, board):
            c = count_onward_moves(nx, ny, board)
            if c < min_deg:
                min_deg = c
                min_deg_idx = i
    if min_deg_idx == -1:
        return None, None
    return x + MOVE_X[min_deg_idx], y + MOVE_Y[min_deg_idx]

def knights_tour(start_x, start_y):
    board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    x, y = start_x, start_y
    board[y][x] = 0
    for move in range(1, BOARD_SIZE * BOARD_SIZE):
        x, y = next_move(x, y, board)
        if x is None:
            return None
        board[y][x] = move
    return board

def draw_board(screen, board, font):
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            color = WHITE if (x + y) % 2 == 0 else GRAY
            pygame.draw.rect(screen, color, rect)
            if board[y][x] != -1:
                text = font.render(str(board[y][x]), True, BLUE)
                screen.blit(text, (x * SQUARE_SIZE + 25, y * SQUARE_SIZE + 25))
    pygame.display.flip()

def animate_knight_tour(path_board):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Knight's Tour")
    font = pygame.font.SysFont(None, FONT_SIZE)

    for move_number in range(BOARD_SIZE * BOARD_SIZE):
        for y in range(BOARD_SIZE):
            for x in range(BOARD_SIZE):
                if path_board[y][x] == move_number:
                    draw_board(screen, path_board, font)
                    pygame.draw.circle(
                        screen,
                        (255, 0, 0),
                        (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2),
                        10,
                    )
                    pygame.display.flip()
                    time.sleep(DELAY)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

# Run the tour and animate
start_x, start_y = 0, 0
board_result = knights_tour(start_x, start_y)
if board_result:
    animate_knight_tour(board_result)
else:
    print("No solution found.")

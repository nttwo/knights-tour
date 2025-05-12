# Knight's Tour Visualization with Pygame

This project visualizes the Knight's Tour on a chessboard using Warnsdorff’s Rule, animated with a graphical interface built using Pygame.

##  What is the Knight's Tour?
import pygame, sys
import imageio
from knights_tour import knights_tour, BOARD_SIZE, SQUARE_SIZE, DRAW_BOARD, animate_frame

# Run the tour logic
board, path = knights_tour(0, 0)

# Initialize Pygame surface for off-screen rendering
pygame.init()
screen = pygame.Surface((BOARD_SIZE * SQUARE_SIZE, BOARD_SIZE * SQUARE_SIZE))
font = pygame.font.SysFont(None, 24)

frames = []

# Capture each frame
for move_number in range(len(path)):
    # Draw board state
    DRAW_BOARD(screen, board, font, move_number)
    # Draw path and knight
    animate_frame(screen, board, path, move_number)
    # Extract image buffer
    raw_str = pygame.image.tostring(screen, 'RGB')
    image = pygame.image.fromstring(raw_str, screen.get_size(), 'RGB')
    arr = pygame.surfarray.array3d(image)
    frames.append(arr)

# Save as GIF
gif_path = 'assets/demo.gif'
imageio.mimsave(gif_path, frames, fps=5)
print(f"Demo GIF saved to {gif_path}")

The Knight's Tour is a classic chess problem in which the knight must visit every square on the board exactly once.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Running the App
```bash
python knights_tour.py
````

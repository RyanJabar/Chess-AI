import pygame
from chess.constants import SQUARE_SIZE, ROWS, COLS, LIGHT_BROWN

'''
self.board variable will be an array of smaller arrays representing each row. Within these inner arrays, the value will represent each individual square

ie. 
[
[a, b, c, d, e, f, g, h]
]
'''

class Board():
    def __init__(self):
        self.board = [
          ['bR', 'bB', 'bN', 'bQ', 'bK', 'bN', 'bB', 'bR'],
          ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP',],
          ['--', '--', '--', '--', '--', '--', '--', '--'],
          ['--', '--', '--', '--', '--', '--', '--', '--'],
          ['--', '--', '--', '--', '--', '--', '--', '--'],
          ['--', '--', '--', '--', '--', '--', '--', '--'],
          ['wP', 'wP', 'wP','wP','wP','wP','wP','wP','wP'],
          ['wR', 'wB', 'wN', 'wQ', 'wK', 'wN', 'wB', 'wR']
        ]

    def draw_squares(self, win):
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, LIGHT_BROWN,
                                 (row * SQUARE_SIZE, col * SQUARE_SIZE,
                                  SQUARE_SIZE, SQUARE_SIZE))
    
    def square_name(self): 
      pass
import pygame
from chess.constants import FPS, WIDTH, HEIGHT, BROWN
from chess.board import Board
from chess.piece import Piece

pygame.init()

board = Board()
piece = Piece("blue")

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Test")
win.fill(BROWN)
board.draw_squares(win)


running = True
while running:

    pygame.display.update()
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

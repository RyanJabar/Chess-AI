from chess.constants import SQUARE_SIZE
from chess.board import Board
import pygame


class Piece():

    def __init__(self, color):
        self.color = color

        self.row = 0
        self.col = 0
        self.x = 0
        self.y = 0

        self.board = Board().board
      
        self.images = {}
        self.calc_pos()
      
    def calc_pos(self):

        for rows in range(len(self.board)):
            for cols in range(len(self.board[rows])):
                #board[rows][cols] method to get individual piece location
                #Assigns each piece an image using a dictionary 
                if self.board[rows][cols] != '--':
                  self.images[self.board[rows][cols]] = pygame.image.load(
                    f"/home/runner/Chess-AI-with-API/piece_images/{self.board[rows][cols]}.png")

    def draw(self, screen):
        s = screen
        for rows in range(len(self.board)): 
            for cols in range(len(self.board[rows])): 
              
              self.x = SQUARE_SIZE * cols + SQUARE_SIZE // 2
              self.y = SQUARE_SIZE * rows + SQUARE_SIZE // 2
          
            for piece in self.images.keys():
                s.blit(self.images[piece], (self.x, self.y))

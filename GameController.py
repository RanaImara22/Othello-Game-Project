from board import Board
from Game import Game
import math

class GameController:
    def __init__(self, depth):
        self.board = Board()
        self.game = Game(self.board)
        self.playerTurn = 'U' #black disks
        self.depth = depth

    def flipDisk(self, x, y, color):
        # moving down
        if (self.board.get_cell(x + 1, y) != color and self.board.get_cell(x + 1, y) != '_'):
            index = x + 1
            flip = False
            for i in range(x + 1, 9):
                if (self.board.get_cell(i, y) == color):
                    flip = True
                    index = i
                    break
            
            if (flip):
                for j in range(x + 1, index + 1):
                    self.board.set_cell(j, y, color)

        # moving up
        if (self.board.get_cell(x - 1, y) != color and self.board.get_cell(x - 1, y) != '_'):
            index = x - 1
            flip = False
            for i in range(x - 1, 0, -1):
                if (self.board.get_cell(i, y) == color):
                    flip = True
                    index = i
                    break
            
            if (flip):
                for j in range(x - 1, index - 1, -1):
                    self.board.set_cell(j, y, color)

        # moving right
        if (self.board.get_cell(x, y + 1) != color and self.board.get_cell(x, y + 1) != '_'):
            index = y + 1
            flip = False
            for i in range(y + 1, 9):
                if (self.board.get_cell(x, i) == color):
                    flip = True
                    index = i
                    break
            
            if (flip):
                for j in range(y + 1, index + 1):
                    self.board.set_cell(x, j, color)

        # moving left
        if (self.board.get_cell(x, y - 1) != color and self.board.get_cell(x, y - 1) != '_'):
            index = y - 1
            flip = False
            for i in range(y - 1, 0, -1):
                if (self.board.get_cell(x, i) == color):
                    flip = True
                    index = i
                    break
            
            if (flip):
                for j in range(y - 1, index - 1, -1):
                    self.board.set_cell(x, j, color)



    def updateBoard(self,x, y, color):
        if (self.board.isLegalMove(x, y, color)):
            self.board.set_cell(x, y, color)
            self.board.printBoard()
            print('\n')
            self.flipDisk(x, y, color)
            self.board.printBoard()

    def switchPlayers(self):
        if (self.playerTurn == 'U'):
            self.playerTurn = 'C' # white

        else:
            self.playerTurn = 'U' # black

    def play(self):
        if (self.playerTurn == 'U'):
            print("\nEnter the coordinates of your desired cell: ")
            x = int(input("x: "))
            y = int(input("y: "))
            self.updateBoard(x, y, 'B')
            self.switchPlayers()

        else:
            evalutation, bestMove = self.game.alphaBetaSearch(self.depth, -1000, 1000, False)
            self.updateBoard(bestMove[0], bestMove[1], 'W')
            self.switchPlayers()

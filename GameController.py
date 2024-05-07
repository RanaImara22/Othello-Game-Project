from board import Board
from Game import Game
import math


class GameController:
    def __init__(self, depth):

        self.board = Board()
        self.game = Game()
        self.playerTurn = 'U' #User Turn 'with black disks'
        self.depth = depth
        self.white = 2
        self.black = 2

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
        self.board.set_cell(x, y, color)
        self.board.printBoard()
        print('\n')
        self.flipDisk(x, y, color)
        self.board.printBoard()
        print('\n')

    def switchPlayers(self):
        if (self.playerTurn == 'U'):
            self.playerTurn = 'C' # white

        else:
            self.playerTurn = 'U' # black

    def play(self):
        gameOver = False
        if (self.white == 2 and self.black == 2):
            print(f"Score:\n White: {self.white}    Black: {self.black}\n")
        if (self.playerTurn == 'U'):
            validMove = False
            while(validMove == False):
                print("\nEnter the coordinates of your desired cell: ")
                x = int(input("x: "))
                y = int(input("y: "))
                validMove = self.board.isLegalMove(x, y, 'B')
                if (validMove == False):
                    print("Invalid Cell. Please Choose Another One")

            self.updateBoard(x, y, 'B')
            self.white, self.black = self.calcScore()
            if (self.isGameOver()):
                gameOver = True
            self.switchPlayers()

        else:
            evalutation, bestMove = self.game.alphaBetaSearch(self.board, self.depth, -1000, 1000, False)
            self.updateBoard(bestMove[0], bestMove[1], 'W')
            self.white, self.black = self.calcScore()
            if (self.isGameOver()):
                gameOver = True
            self.switchPlayers()

        if (gameOver):
            if (self.black > self.white):
                print(f"YOU WON. \n Black Disks = {self.black} and White Disks = {self.white}\n")
            elif (self.white > self.black):
                print(f"COMPUTER WON. \n Black Disks = {self.black} and White Disks = {self.white}\n")
            else:
                print(f"TIE. \n Black Disks = {self.black} and White Disks = {self.white}\n")
        else:
            print(f"Score:\n White: {self.white}    Black: {self.black}\n")

    def isGameOver(self):
        for i in range(1, 9):
            for j in range(1, 9):
                if (self.board.get_cell(i, j) == '_'):
                    return False
        return True

    def calcScore(self):
        self.white = 0
        self.black = 0
        for i in range(1, 9):
            for j in range(1, 9):
                if (self.board.get_cell(i, j) == 'B'):
                    self.black += 1
                elif (self.board.get_cell(i, j) == 'W'):
                    self.white += 1

        return self.white, self.black

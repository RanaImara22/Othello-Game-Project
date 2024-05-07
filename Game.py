import math
import copy

from board import Board


class Game:
    # def __init__(self, board):
    #     self.coBoard = board
    #     # self.coBoard.copy_board(board)


    def utilityFunc(self, board):
        # Black is MAX and White is MIN
        white = 0
        black = 0
        for i in range(1, 9):
            for j in range(1, 9):
                if (board.get_cell(i, j) == 'W'):
                    white += 1
                elif (board.get_cell(i, j) == 'B'):
                    black += 1

        return black - white

    def getValidChildren(self, board, isMaxPlayer):
        playerColor = 'B'
        if (isMaxPlayer == False): # color is white
            playerColor = 'W'
        validChildren = []
        for i in range(1, 9):
            for j in range(1, 9):
                if (board.isLegalMove(i, j, playerColor)):
                    validChildren.append((i, j))

        return validChildren


    # A duplicate function as used in gameController, but to avoid circular dependency between
    # GameController and Game
    # Only difference that it takes 'board' attribute
    def flipDisk(self, board, x, y, color):
        # moving down
        if (board.get_cell(x + 1, y) != color and board.get_cell(x + 1, y) != '_'):
            index = x + 1
            flip = False
            for i in range(x + 1, 9):
                if (board.get_cell(i, y) == color):
                    flip = True
                    index = i
                    break
            
            if (flip):
                for j in range(x + 1, index + 1):
                    board.set_cell(j, y, color)

        # moving up
        if (board.get_cell(x - 1, y) != color and board.get_cell(x - 1, y) != '_'):
            index = x - 1
            flip = False
            for i in range(x - 1, 0, -1):
                if (board.get_cell(i, y) == color):
                    flip = True
                    index = i
                    break
            
            if (flip):
                for j in range(x - 1, index - 1, -1):
                    board.set_cell(j, y, color)

        # moving right
        if (board.get_cell(x, y + 1) != color and board.get_cell(x, y + 1) != '_'):
            index = y + 1
            flip = False
            for i in range(y + 1, 9):
                if (board.get_cell(x, i) == color):
                    flip = True
                    index = i
                    break
            
            if (flip):
                for j in range(y + 1, index + 1):
                    board.set_cell(x, j, color)

        # moving left
        if (board.get_cell(x, y - 1) != color and board.get_cell(x, y - 1) != '_'):
            index = y - 1
            flip = False
            for i in range(y - 1, 0, -1):
                if (board.get_cell(x, i) == color):
                    flip = True
                    index = i
                    break
            
            if (flip):
                for j in range(y - 1, index - 1, -1):
                    board.set_cell(x, j, color)




    def alphaBetaSearch(self, board, depth, alpha, beta, isMaxPlayer):
        if (depth == 0):
            return self.utilityFunc(board), None
        
        children = self.getValidChildren(board, isMaxPlayer)
        if (isMaxPlayer):
            maxEval = -1000
            bestChild = None
            for child in children:
                child_board = copy.deepcopy(board)  
                child_board.set_cell(child[0], child[1], 'B') 
                self.flipDisk(child_board, child[0], child[1], 'B')
                evalutation, _ = self.alphaBetaSearch(child_board, depth - 1, alpha, beta, False)
                # print(f"child: ({child[0]}, {child[1]}), evalutaion: {evalutation} \n")
                if (maxEval < evalutation):
                    maxEval = evalutation
                    bestChild = child
                alpha = max(alpha, evalutation)
                if (beta <= alpha):
                    break
            # print(f"Best Child: ({bestChild[0]}, {bestChild[1]}), Max evalutaion: {maxEval} \n")
            return maxEval, bestChild

        else:
            minEval = 1000
            bestChild = None
            for child in children:
                child_board = copy.deepcopy(board)  
                child_board.set_cell(child[0], child[1], 'W') 
                self.flipDisk(child_board, child[0], child[1], 'W')
                evalutation, _ = self.alphaBetaSearch(child_board, depth - 1, alpha, beta, True)
                # print(f"child: ({child[0]}, {child[1]}), evalutaion: {evalutation} \n")
                if (minEval > evalutation):
                    minEval = evalutation
                    bestChild = child
                beta = min(beta, evalutation)
                if (beta <= alpha):
                    break
            # print(f"Best Child: ({bestChild[0]}, {bestChild[1]}), Min evalutaion: {minEval} \n")
            return minEval, bestChild


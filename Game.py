import math

class Game:
    def __init__(self, board):
        self.coBoard = board

    def utilityFunc(self):
        # Black is MAX and White is MIN
        white = 0
        black = 0
        for i in range(1, 9):
            for j in range(1, 9):
                if (self.coBoard.get_cell(i, j) == 'W'):
                    white += 1
                elif (self.coBoard.get_cell(i, j) == 'B'):
                    black += 1

        return black - white

    def getValidChildren(self, isMaxPlayer):
        playerColor = 'B'
        if (isMaxPlayer == False): # color is white
            playerColor = 'W'
        validChildren = []
        for i in range(1, 9):
            for j in range(1, 9):
                if (self.coBoard.isLegalMove(i, j, playerColor)):
                    validChildren.append((i, j))

        return validChildren

    def isGameOver(self):
        for i in range(1, 9):
            for j in range(1, 9):
                if (self.coBoard.get_cell(i, j) == '_'):
                    return False
        return True

    
    def alphaBetaSearch(self, depth, alpha, beta, isMaxPlayer):
        if (depth == 0 or self.isGameOver()):
            return self.utilityFunc(), None
        
        children = self.getValidChildren(isMaxPlayer)
        if (isMaxPlayer):
            maxEval = -math.inf
            bestChild = None
            for child in children:
                evalutation, _ = self.alphaBetaSearch( depth - 1, alpha, beta, False)
                maxEval = max(maxEval, evalutation)
                alpha = max(alpha, evalutation)
                bestChild = child
                if (beta <= alpha):
                    break
            return maxEval, bestChild

        else:
            minEval = math.inf
            bestChild = None
            for child in children:
                evalutation, _ = self.alphaBetaSearch( depth - 1, alpha, beta, True)
                minEval = max(minEval, evalutation)
                beta = max(beta, evalutation)
                bestChild = child
                if (beta <= alpha):
                    break
            return minEval, bestChild


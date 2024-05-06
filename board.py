class Board:
    

    def __init__(self):
        self.board = [['_' for _ in range(10)] for _ in range(10)]
        self.board[4][4] = 'W'
        self.board[4][5] = 'B'
        self.board[5][4] = 'B'
        self.board[5][5] = 'W'
        self.printBoard()

    def printBoard(self):
        for i in range(1, 9):
            for j in range(1, 9):
                print(self.board[i][j] + "  ", end="")

            print('\n')

    def isLegalMove(self, x, y, color):
        oppColor = 'B'
        if(color == 'B'):
            oppColor = 'W'
        if (self.get_cell(x, y) == '_' and (self.get_cell(x + 1, y) == oppColor or
        self.get_cell(x - 1, y) == oppColor or self.get_cell(x, y + 1) == oppColor or
        self.get_cell(x, y - 1) == oppColor)):
            return True
        return False

    def get_cell(self, x, y):
        return self.board[x][y]

    def set_cell(self, x, y, value):
        self.board[x][y] = value

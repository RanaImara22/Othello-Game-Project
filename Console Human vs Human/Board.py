class Board:
    def __init__(self, size=8):
        self.size = size
        self.board = [['.' for _ in range(size)] for _ in range(size)]
        self.init_board()

    def init_board(self):
        mid = self.size // 2
        self.board[mid][mid] = 'W'
        self.board[mid - 1][mid - 1] = 'W'
        self.board[mid][mid - 1] = 'B'
        self.board[mid - 1][mid] = 'B'


    def check_end_game(self):
        for row in self.board:
            if '.' in row:
                return False
        return True

    def valid_moves(self, player):
        opponent = 'B' if player.color == 'W' else 'W'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        size = len(self.board)
        valid_cells = []
        for x in range(size):
            for y in range(size):
                if self.board[x][y] == player.color:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < size and 0 <= ny < size and self.board[nx][ny] == opponent:
                            while 0 <= nx < size and 0 <= ny < size and self.board[nx][ny] == opponent:
                                nx += dx
                                ny += dy
                            if 0 <= nx < size and 0 <= ny < size and self.board[nx][ny] == '.':
                                valid_cells.append((nx, ny))

        return list(set(valid_cells))

    def show_board(self):
        print("  0 1 2 3 4 5 6 7")
        for i in range(8):
            print(i, end='.')
            for j in range(8):
                print(self.board[i][j], end='.')
            print()

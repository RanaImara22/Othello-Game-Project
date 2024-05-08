from Board import Board
from Player import Player


class GameController:
    def __init__(self):
        self.players = []
        self.board = Board()
        self.current_player = None

    def start(self):
        self.make_player()
        self.play()

    def play(self):
        while not self.board.check_end_game():
            self.board.show_board()
            x, y = self.get_move()
            if x != -1 and y != -1:
                self.board.add_disk(self.current_player, x, y)
                self.update_score()

            self.switch_player()
        if self.players[0].score > self.players[1].score:
            print(f"{self.players[0].name} win ")
        elif self.players[0].score == self.players[1].score:
            print("Game is Draw")
        else:
            print(f"{self.players[1].name} win ")

    def make_player(self):
        first_name = input("Enter the first name for Player 1: ")
        second_name = input("Enter the first name for Player 2: ")

        player1 = Player(first_name, 'B')
        player2 = Player(second_name, 'W')

        self.players.append(player1)
        self.players.append(player2)

        self.current_player = player1

    def switch_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def get_move(self):
        print(
            f"Scores: {self.players[0].name} (B): {self.players[0].score}, {self.players[1].name} (W): {self.players[1].score}")
        print(f"Player {self.current_player.name}'s turn ({self.current_player.color}):")
        valid_moves = self.board.valid_moves(self.current_player)
        if len(valid_moves) > 0:
            print(f"valid cells {valid_moves}")
            while True:
                x = int(input("Enter row: "))
                y = int(input("Enter column: "))
                cell = (x, y)

                if cell in valid_moves:
                    return cell
                else:
                    print("Invalid move. Please choose a valid cell.")
        return -1, -1

    def update_score(self):
        self.players[0].score = sum(row.count(self.players[0].color) for row in self.board.board)
        self.players[1].score = sum(row.count(self.players[1].color) for row in self.board.board)

    def add_disk(self, x, y):
        self.board.board[x][y] = self.current_player.color
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            if self.is_valid_direction(x, y, dx, dy):
                self.flip(x, y, dx, dy)

    def is_valid_direction(self, x, y, dx, dy):
        x += dx
        y += dy
        if x < 0 or x >= 8 or y < 0 or y >= 8 or self.board.board[x][y] == '.' or self.board.board[x][y] == self.current_player.color:
            return False
        while 0 <= x < 8 and 0 <= y < 8:
            if self.board.board[x][y] == self.current_player.color:
                return True
            if self.board.board[x][y] == '.':
                return False
            x += dx
            y += dy
        return False

    def flip(self, x, y, dx, dy):
        x += dx
        y += dy
        while 0 <= x < 8 and 0 <= y < 8:
            if self.board.board[x][y] == self.current_player.color:
                return
            self.board.board[x][y] = self.current_player.color
            x += dx
            y += dy


game = GameController()
game.start()

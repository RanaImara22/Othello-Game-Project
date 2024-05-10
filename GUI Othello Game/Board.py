import tkinter as tk
from tkinter import font as tkfont

from Button import Button 
class GameBoard:
    def __init__(self, game_controller, players):
        self.buttons = [[Button for i in range(8)] for j in range(8)]
        self.window = tk.Tk()
        self.window.title("Othello Game - Playing")
        # self.window.geometry("350x500")
        self.window.resizable(True, False)
        self.window.configure(bg="green")
        self.game_controller = game_controller
        self.players = players
        self.player_labels = []
        self.init_game_board()

    def createBoard(self , grid):
        for i in range(8):
            for j in range(8):
                self.buttons[i][j] = Button(grid, i , j , '.' , self.game_controller.clicked)
        self.buttons[3][3].change_oval_color('W')
        self.buttons[3][4].change_oval_color('B')
        self.buttons[4][3].change_oval_color('B')
        self.buttons[4][4].change_oval_color('W')
    def init_game_board(self):
        # Create player labels and scores
        for index, player in enumerate(self.players, start=1):
            player_label = tk.Label(self.window, text=player.name + " (" + player.color + ")", 
                                    font=tkfont.Font(weight="bold", family="Sedan AC", size=10),
                                    bg="green", fg="white")
            if(index == 1) : player_label.grid(row=0, column=index , cnf={'sticky': 'w'}, padx=len(player.name)  + 20, pady=2)
            else :
                player_label.grid(row=0, column=index , cnf={'sticky': 'w'}, pady=2)
            player_score = tk.Label(self.window, text=str(player.score), 
                                    font=tkfont.Font(weight="bold", family="Sedan AC", size=10),
                                    bg="green", fg="white")
            player_score.grid(row=1, column=index, padx=len(player.name) * index + 20, pady=2)
            self.player_labels.append(player_score)

        current_player_label = tk.Label(self.window, text="Current Player: " + self.players[0].name ,name="current_player_label",)
        current_player_label.grid(row=2, column=0, columnspan=len(self.players)+1, padx=10, pady=5)

        # Create game board canvas
        game_board = tk.Canvas(self.window, width=350, height=500, bg="green")
        game_board.grid(row=3, column=1, columnspan=len(self.players)+1, padx=10, pady=10)

        # Create reset button
        reset_button = tk.Button(self.window, width=20, text="Reset Game", command=self.game_controller.reset_game)
        reset_button.grid(row=4, column=1, columnspan=len(self.players)+1, padx=10, pady=5)

        # Draw game board grid
        game_board.create_rectangle(0, 0, 350, 500, fill="green")
        self.createBoard(game_board)

    def display_valid_moves(self, valid_moves):
        for move in valid_moves:
            x, y = move[0]
            self.buttons[x][y].makeHover()
            self.buttons[x][y].button.bind("<Enter>", lambda event, move=move: self.display_modified_cells(move , self.game_controller.players[self.game_controller.current_player].color))
            self.buttons[x][y].button.bind("<Leave>", lambda event, move=move: self.remove_modified_cells(move))


    def display_modified_cells(self, modified_cells, color):
        self.buttons[modified_cells[0][0]][modified_cells[0][1]].change_oval_color(color , True)
        for cell in modified_cells[1]:
            x, y = cell
            self.buttons[x][y].change_oval_color(color , True)

    def remove_modified_cells(self, modified_cells):
        self.buttons[modified_cells[0][0]][modified_cells[0][1]].makeHover()
        for cell in modified_cells[1]:
            x, y = cell
            self.buttons[x][y].resetColor()

    def remove_valid_moves(self, valid_moves):
        for move in valid_moves:
            x, y = move[0]
            self.buttons[x][y].resetColor()
            self.buttons[x][y].button.unbind("<Enter>")
            self.buttons[x][y].button.unbind("<Leave>")

    def change_current_player_label(self, player):
        color = "Black" if player.color == 'B' else "White"
        self.window.children["current_player_label"].config(text="Current Player: " + player.name + " (" + color  + ")")


    def change_score(self, players):
        for index, player in enumerate(players):
            self.player_labels[index].config(text=str(player.score))

    def reset_board(self):
        for i in range(8):
            for j in range(8):
                self.buttons[i][j].change_oval_color('.')
        self.buttons[3][3].change_oval_color('W')
        self.buttons[3][4].change_oval_color('B')
        self.buttons[4][3].change_oval_color('B')
        self.buttons[4][4].change_oval_color('W')
        self.players[0].score = 2
        self.players[1].score = 2
        self.player_labels[0].config(text="2")
        self.player_labels[1].config(text="2")

    def copy_board(self , board , fake = False):
        new_board = []
        for i in range(8):
            new_board.append([])
            for j in range(8):
                if(fake == False):
                    new_board[i].append(board[i][j].color)
                else:
                    new_board[i].append(board[i][j])
        return new_board

    def get_cell_color(self, x, y):
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            return 0
        return self.buttons[x][y].color
    
    def updateGUI(self):
        self.window.update()
    
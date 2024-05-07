import tkinter as tk
from tkinter import font as tkfont 
class GameBoard:
    def __init__(self, game_controller, players):
        self.window = tk.Tk()
        self.window.title("Othello Game - Playing")
        self.window.geometry("420x500")
        self.window.resizable(False, False)
        self.window.configure(bg="green")
        self.game_controller = game_controller
        self.players = players
        self.player_labels = []
        self.buttons = [[0 for i in range(8)] for j in range(8)]
        self.buttons[3][3] = 'W'
        self.buttons[3][4] = 'B'
        self.buttons[4][3] = 'B'
        self.buttons[4][4] = 'W'
        self.current_player_label = tk.Label(self.window, text="Current Player: ") 
        self.current_player_label.grid(row=1, column=0, columnspan=2) 
        self.init_game_board()

    def getBoardCopy(self):
        boardCopy = [[0 for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                color = self.get_cell_color(i, j)
                boardCopy[i][j] = color
        return boardCopy
        
        # . B W

    # def init_game_board(self):
    #     #labels with a different text and color of text is black

    #     player1_label = tk.Label(self.window, text=self.players[0].name + " Score " + str(self.players[0].score) ,font= tkfont.Font(weight= "bold" , family="Arial" , size=10) , bg="green", fg="white")
    #     player2_label = tk.Label(self.window, text=self.players[1].name + " Score " + str(self.players[1].score) ,font= tkfont.Font(weight= "bold" , family="Arial" , size=10), bg="green", fg="white")
    #     player1_label.grid(row=0, column=0)
    #     player2_label.grid(row=0, column=1) 
    #     self.player_labels = [player1_label, player2_label]
    #     self.current_player_label.config(text="Current Player: " + self.game_controller.current_player['player'].name)
    #     game_board = tk.Canvas(self.window, width=200, height=200, bg="green")
    #     game_board.grid(row=2, column=1 ,pady=10)
    #     reset_button = tk.Button(self.window, width=40, text="Reset Game", command=self.game_controller.reset_game)
    #     reset_button.grid(row=3, column=0)
    #     game_board.create_rectangle(0, 0, 500, 500, fill="green")
    #     for i in range(8):
    #         for j in range(8):
    #             button = tk.Button(game_board, width=6, height=3,
    #                                 command=lambda i=i, j=j: self.game_controller.clicked(i, j , self.game_controller.current_player), compound='center'  , bg="darkgray" , state="normal" , padx=1 , pady=1)
    #             button.grid(row=i, column=j)
    #             if self.buttons[i][j] == 'W':
    #                 button.config(borderwidth=0 , bg="white" ,  state="disabled")
    #             elif self.buttons[i][j] == 'B':
    #                 button.config(borderwidth=0 , bg="black" , state="disabled")
    #             self.buttons[i][j] = button

    def init_game_board(self):
        # Player 1 name and score
        player1_label = tk.Label(self.window, text=self.players[0].name,
                                font=tkfont.Font(weight="bold", family="Sedan AC", size=10),bg="green" , fg="white")
        player1_label.grid(row=0, column=0, padx=10, pady=5)
        # Player 1 score
        player1_score = tk.Label(self.window, text=str(self.players[0].score) , font=tkfont.Font(weight="bold", family="Sedan AC", size=10),bg="green" , fg="white"  )
        player1_score.grid(row=1, column=0, padx=10, pady=5)

        # Player 2 name and score
        player2_label = tk.Label(self.window, text=self.players[1].name,
                                font=tkfont.Font(weight="bold", family="Sedan AC", size=10), bg="green" , fg="white")
        player2_label.grid(row=0, column=1, padx=10, pady=5)
        # Player 2 score
        player2_score = tk.Label(self.window, text=str(self.players[1].score) , font=tkfont.Font(weight="bold", family="Sedan AC", size=10),bg="green" , fg="white")
        player2_score.grid(row=1, column=1, padx=10, pady=5)
        self.player_labels = [player1_score, player2_score]

        # Current player label
        self.current_player_label.config(text="Current Player: " + self.game_controller.current_player['player'].name)
        self.current_player_label.grid(row=2, column=0, columnspan=2, padx=(40, 0) ,pady=5)

        # Game board canvas
        game_board = tk.Canvas(self.window, width=400, height=400, bg="green")
        game_board.grid(row=3, column=0, columnspan=2, padx=(40, 0), pady=10)

        # Reset button
        reset_button = tk.Button(self.window, width=20, text="Reset Game", command=self.game_controller.reset_game)
        reset_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Draw game board grid
        game_board.create_rectangle(0, 0, 400, 400, fill="green")
        for i in range(8):
            for j in range(8):
                # Create circular buttons
                radius = 20  # Adjust radius as needed
                x0 = j * 50 + 10  # Adjust horizontal spacing
                y0 = i * 50 + 10  # Adjust vertical spacing
                x1 = x0 + radius
                y1 = y0 + radius
                button = tk.Canvas(game_board, width=2*radius, height=2*radius, bg="darkgray", highlightthickness=0)
                button.create_oval(5, 5, 35, 35, fill="lightgray")  # Draw circle
                button.grid(row=i, column=j, padx=1, pady=1)
                button.bind("<Button-1>", lambda event , i=i , j = j  : self.game_controller.clicked(i, j, self.game_controller.current_player ))
                if self.buttons[i][j] == 'W':
                    button.create_oval(5, 5, 35, 35, fill="white" , state="disabled")  # White piece
                elif self.buttons[i][j] == 'B':
                    button.create_oval(5, 5, 35, 35, fill="black", state="disabled")  # Black piece
                else :
                    button.create_oval(5, 5, 35, 35, fill="darkgray" , state="normal")
                self.buttons[i][j] = button

    def display_valid_moves(self, valid_moves):
        for move in valid_moves:
            self.buttons[move[0]][move[1]].create_oval(5, 5, 35, 35, fill="yellow")

    def remove_valid_moves(self, valid_moves):
        for move in valid_moves:
            self.buttons[move[0]][move[1]].create_oval(5, 5, 35, 35, fill="darkgray")

    def reset_board(self):
        for i in range(8):
            for j in range(8):
                self.buttons[i][j].delete("all")
                self.buttons[i][j].create_oval(5, 5, 35, 35, fill="darkgray")
                self.buttons[i][j].config(state="normal")
        self.buttons[3][3].create_oval(5, 5, 35, 35, fill="white")
        self.buttons[3][4].create_oval(5, 5, 35, 35, fill="black")
        self.buttons[4][3].create_oval(5, 5, 35, 35, fill="black")
        self.buttons[4][4].create_oval(5, 5, 35, 35, fill="white")
        self.players[0].score = 2
        self.players[1].score = 2
        self.player_labels[0].config(text=str(self.players[0].score))
        self.player_labels[1].config(text=str(self.players[1].score))



    def change_oval_color(self, button , player):
        oval_id = button.find_all()[-1]
        newColor = player.color == 'B' and "black" or "white"
        button.itemconfig(oval_id, fill=newColor)

    def add_disk(self, x, y , player , board = None):
        if board : board[x][y] = player.color
        else :
            button = self.buttons[x][y]
            self.change_oval_color(button , player)
        if board == None : player.score += 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            if self.is_valid_direction(x, y, dx, dy, player , board):
                self.flip(x, y, dx, dy, player , board)



    def is_valid_direction(self, x, y, dx, dy, player , board = None):
        x += dx
        y += dy
        cellColor = self.get_cell_color(x, y , board)
        if x < 0 or x >= 8 or y < 0 or y >= 8 or cellColor == '.' or cellColor == player.color:
            return False
        while 0 <= x < 8 and 0 <= y < 8:
            cellColor = self.get_cell_color(x, y , board)
            if cellColor == player.color:
                return True
            if cellColor == '.':
                return False
            x += dx
            y += dy
        return False
    

    def flip(self, x, y, dx, dy, player , board = None):
        x += dx
        y += dy
        while 0 <= x < 8 and 0 <= y < 8:
            cellColor = self.get_cell_color(x, y , board)
            if cellColor == player.color:
                return
            if(cellColor != '.' and board == None):
                if(player.color == 'B'):
                    self.players[1].score -= 1
                    self.players[0].score += 1 
                else:
                    self.players[0].score -= 1
                    self.players[1].score += 1
            if(board): board[x][y] = player.color
            else: self.change_oval_color(self.buttons[x][y], player)
            x += dx
            y += dy


    def check_end_game(self):
        for row in self.buttons:
            for cell in row:
                if cell.cget('bg') == "darkgray":
                    return False
        return True

    def valid_moves(self, player , board = None):
        opponent = 'B' if player.color == 'W' else 'W'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        valid_cells = []
        for x in range(8):
            for y in range(8):
                cellColor = self.get_cell_color(x, y , board)
                if cellColor == player.color:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        newCellColor = self.get_cell_color(nx, ny , board)
                        if 0 <= nx < 8 and 0 <= ny < 8 and newCellColor == opponent:
                            while 0 <= nx < 8 and 0 <= ny < 8 and newCellColor == opponent:
                                nx += dx
                                ny += dy
                                if 0 <= nx < 8 and 0 <= ny < 8:
                                     newCellColor = self.get_cell_color(nx, ny , board)
                            if 0 <= nx < 8 and 0 <= ny < 8 and newCellColor == '.':
                                valid_cells.append((nx, ny))
        return list(set(valid_cells))


    def get_cell_color(self, x, y , board = None):
        if(x < 0 or x >= 8 or y < 0 or y >= 8): return 0
        if board : return board[x][y]
        else :
            button_color = self.buttons[x][y].itemcget(self.buttons[x][y].find_all()[-1], "fill")
            if button_color == "darkgray" or button_color == "yellow":
                return '.'
            elif button_color == 'black':
                return 'B'
            else:
                return 'W'
    def updateGUI(self):
        self.window.update()
    
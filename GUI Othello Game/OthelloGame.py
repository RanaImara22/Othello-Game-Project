# import tkinter as tk
# from tkinter import messagebox

# from Classes.GameController import GameController
# from Classes.Player import Player

# class OthelloGame:
#     def __init__(self):
#         self.players = []
#         self.buttons = [[0 for i in range(8)] for j in range(8)]
#         self.buttons[3][3] = 'W'
#         self.buttons[3][4] = 'B'
#         self.buttons[4][3] = 'B'
#         self.buttons[4][4] = 'W'
#         self.current_player = None
#         self.current_player_label = None
#         self.gameController = None

#     def clicked(self, i, j): 
#         valid_moves = self.gameController.moves(self.current_player)
#         if (i, j) not in valid_moves:
#             messagebox.showinfo("Invalid Move", "Invalid Move")
#             return
#         self.remove_valid_moves(valid_moves)
#         self.gameController.play(i, j , self.current_player)
#         if self.gameController.board.check_end_game():
#             self.show_winner()
#             return
#         self.switch_player()
#         self.change_score()
#         valid_moves = self.gameController.moves(self.current_player)
#         if not valid_moves:
#             messagebox.showinfo("No Valid Move", "No Valid Move")
#             self.switch_player()
#             valid_moves = self.gameController.moves(self.current_player)
#             if not valid_moves:
#                 self.show_winner()
#                 return
#         self.display_valid_moves(valid_moves)

#     def show_winner(self):
#         if self.players[0].score > self.players[1].score:
#             messagebox.showinfo("Winner", self.players[0].name + " is the winner")
#         elif self.players[0].score < self.players[1].score:
#             messagebox.showinfo("Winner", self.players[1].name + " is the winner")
#         else:
#             messagebox.showinfo("Winner", "It's a tie")

#     def reset_game(self):
#         for i in range(8):
#             for j in range(8):
#                 self.buttons[i][j].config(bg="darkgray", state="normal")
#         self.buttons[3][3].config(bg="white", state="disabled")
#         self.buttons[3][4].config(bg="black", state="disabled")
#         self.buttons[4][3].config(bg="black", state="disabled")
#         self.buttons[4][4].config(bg="white", state="disabled")
#         self.players[0].score = 2
#         self.players[1].score = 2
#         self.player1_label.config(text=self.players[0].name + " Score " + str(self.players[0].score))
#         self.player2_label.config(text=self.players[1].name + " Score " + str(self.players[1].score))
#         self.current_player = self.players[0]
#         self.current_player_label.config(text="Current Player: " + self.current_player.name)
#         self.display_valid_moves(self.gameController.moves(self.current_player))

#     def switch_player(self):
#         if self.current_player == self.players[0]:
#             self.current_player = self.players[1]
#         else:
#             self.current_player = self.players[0]
#         self.current_player_label.config(text="Current Player: " + self.current_player.name)

#     def change_score(self):
#         self.player1_label.config(text=self.players[0].name + " Score " + str(self.players[0].score))
#         self.player2_label.config(text=self.players[1].name + " Score " + str(self.players[1].score))

#     def display_valid_moves(self, valid_moves):
#         for move in valid_moves:
#             self.buttons[move[0]][move[1]].config(bg="yellow" )

#     def remove_valid_moves(self, valid_moves):
#         for move in valid_moves:
#             self.buttons[move[0]][move[1]].config(bg="darkgray")

#     def game_window(self, window, player1_func, player2_func=-1, difficulty="Easy"):
#         player1Name = player1_func()
#         player2Name = player2_func()
#         self.players.append(Player(player1Name, 'B'))
#         self.players.append(Player(player2Name, 'W'))
#         window.destroy()
#         game_window = tk.Tk()
#         game_window.title("Othello Game - Playing")
#         game_window.geometry("500x540")
#         game_window.configure(bg="green")
#         self.player1_label = tk.Label(game_window, width=36, text=self.players[0].name + " Score " + str(self.players[0].score), bg="green", fg="white")
#         self.player1_label.grid(row=0, column=0)
#         self.player2_label = tk.Label(game_window, width=36, text=self.players[1].name + " Score " + str(self.players[1].score), bg="green", fg="white")
#         self.player2_label.grid(row=0, column=1)
#         self.current_player = self.players[0]
#         self.current_player_label = tk.Label(game_window, width=36, text="Current Player: " + self.current_player.name, bg="green", fg="white")
#         self.current_player_label.grid(row=1, column=0 , columnspan=2)
#         reset_button = tk.Button(game_window, width=40, text="Reset Game", command=self.reset_game)
#         reset_button.grid(row=3, column=0, columnspan=2)
#         game_board = tk.Canvas(game_window, width=400, height=400, bg="green")
#         game_board.grid(row=2, column=0, columnspan=2, pady=10)
#         game_board.create_rectangle(0, 0, 600, 600, fill="green")
#         for i in range(8):
#             for j in range(8):
#                 button = tk.Button(game_board, width=6, height=3,
#                                     command=lambda i=i, j=j: self.clicked(i, j), compound='center'  , bg="darkgray" , state="normal" , padx=1 , pady=1)
#                 button.grid(row=i, column=j)
#                 if self.buttons[i][j] == 'W':
#                     button.config(borderwidth=0 , bg="white" ,  state="disabled")
#                 elif self.buttons[i][j] == 'B':
#                     button.config(borderwidth=0 , bg="black" , state="disabled")
#                 self.buttons[i][j] = button
#         self.current_player = self.players[0]
#         self.gameController = GameController(self.buttons, self.players)
#         self.display_valid_moves(self.gameController.moves(self.current_player))
#         game_board.mainloop()
#         game_window.mainloop()

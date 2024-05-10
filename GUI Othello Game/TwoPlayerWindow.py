import tkinter as tk
from Player import Player
from GameController import GameController
from tools import textField

class TwoPlayerWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Othello Game - Two Player")
        self.window.geometry("400x70")

        self.p1_entry = textField(self.window, "Player 1 Name :", 0, 0)
        self.p2_entry = textField(self.window, "Player 2 Name :", 1, 0)

        self.start_button = tk.Button(self.window, width=30, text="Start Game", 
                                      command=self.start_game)
        self.start_button.grid(row=2, column=1)

    def start_game(self):
        player1_name = self.p1_entry.get()
        player2_name = self.p2_entry.get()
        players = [Player(player1_name, 'B'), Player(player2_name, 'W')]
        GameController(players , -1)
        self.window.destroy()
        
    def run(self):
        self.window.mainloop()
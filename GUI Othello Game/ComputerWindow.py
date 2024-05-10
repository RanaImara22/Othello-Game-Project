import tkinter as tk
from Player import Player
from GameController import GameController
from tools import textField

class ComputerWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Othello Game - One Player")
        self.window.geometry("400x50")
        self.p1_entry = textField(self.window, "Player 1 Name :", 0, 0)
        self.options = ["Easy", "Medium", "Hard"]
        self.p2_entry = tk.StringVar(self.window)
        self.p2_entry.set(self.options[0])
        self.p2_menu = tk.OptionMenu(self.window, self.p2_entry, *self.options)
        self.p2_menu.grid(row=1, column=0)
        self.start_button = tk.Button(self.window, width=40, text="Start Game", 
                                      command=self.start_game)
        self.start_button.grid(row=1, column=1, columnspan=2)

    def start_game(self):
        player1_name = self.p1_entry.get()
        difficulty = self.p2_entry.get()
        depth = 0
        if difficulty == "Medium":
            depth = 3
        elif difficulty == "Hard":
            depth = 5
        else :
            depth = 1
        players = [Player(player1_name, 'B'), Player("Computer", 'W')]
        othelloGame = GameController(players , depth)
        self.window.destroy()
        
    def run(self):
        self.window.mainloop()
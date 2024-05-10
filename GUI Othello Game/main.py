import tkinter as tk

from ComputerWindow import ComputerWindow
from TwoPlayerWindow import TwoPlayerWindow

class OthelloMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Othello Game")
        self.window.geometry("435x26")

        self.twoPlayerButton = tk.Button(self.window, width=30, text="Two Player Game", command=self.open_two_player_window)
        self.twoPlayerButton.grid(row=0, column=1)
        self.AIPlayerButton = tk.Button(self.window, width=30, text="Play with Computer", command=self.open_computer_window)
        self.AIPlayerButton.grid(row=0, column=2)

    def open_two_player_window(self):
        self.window.destroy()
        TwoPlayerWindow()

    def open_computer_window(self):
        self.window.destroy()
        ComputerWindow()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    menu = OthelloMenu()
    menu.run()

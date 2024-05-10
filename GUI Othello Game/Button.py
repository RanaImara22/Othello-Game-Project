import tkinter as tk
class Button:
    def __init__(self, master , i , j , color, function=None):
        self.button = tk.Canvas(master, width=2 * 20, height=2 * 20, bg="green", highlightthickness=0)
        self.color = color
        if self.color == 'W':
            self.oval_item = self.button.create_oval(5, 5, 35, 35, fill="white")
        elif self.color == 'B':
            self.oval_item = self.button.create_oval(5, 5, 35, 35, fill="black")
        else:
            self.oval_item = self.button.create_oval(5, 5, 35, 35, fill="darkgray")
        self.button.grid(row=i, column=j)
        self.button.bind("<Button-1>", lambda event, i=i, j=j: function(i, j))

    def change_oval_color(self , color , fake = False):
        if color == 'W':
            self.button.itemconfig(self.oval_item, fill="white")
        elif color == 'B':
            self.button.itemconfig(self.oval_item, fill="black")
        else:
            self.button.itemconfig(self.oval_item, fill="darkgray")
        if fake == False : self.color = color

    def makeHover(self):
        self.button.itemconfig(self.oval_item, fill="yellow")
        
    def resetColor(self):
        if self.color == 'W':
            self.button.itemconfig(self.oval_item, fill="white")
        elif self.color == 'B':
            self.button.itemconfig(self.oval_item, fill="black")
        else:
            self.button.itemconfig(self.oval_item, fill="darkgray")

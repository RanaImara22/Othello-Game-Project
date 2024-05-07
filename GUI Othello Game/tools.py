import tkinter as tk

def textField(window, text, row, column):
    label = tk.Label(window, text=text)
    label.grid(row=row, column=column)
    entry = tk.Entry(window, width=50)
    entry.grid(row=row, column=column+1)
    return entry
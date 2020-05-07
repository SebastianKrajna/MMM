import tkinter as tk
from tkinter import ttk

from DataEntry import *


class Window():
    def __init__(self, master):
        self.master = master
        master.title("")
        master.minsize(1000, 500)
        
        self.dataFrame = ttk.LabelFrame(master, text = "Wprowadź dane")
        self.dataFrame.place(x = 5, y = 5, width = 300, height = 500)
        self.dataEntry = DataEntry(self.dataFrame)

        self.drawFrame = ttk.LabelFrame(master, text = "Wykresy")
        self.drawFrame.place(x = 310, y = 5, width = 800, height = 500)


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
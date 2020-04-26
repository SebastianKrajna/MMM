import tkinter as tk
from tkinter import ttk

import DataEntry


class Window():
    def __init__(self, master):
        self.master = master
        master.title("")
        
        self.dataFrame = ttk.LabelFrame(master, text = "Wprowadź dane")
        self.dataFrame.place(x = 5, y = 5, width = 400, height = 500)
        self.dataEntry = DataEntry(self.dataFrame)

        self.drawFrame = ttk.LabelFrame(master, text = "Wykresy")
        self.drawFrame.place(x = 410, y = 5, width = 800, height = 500)

    
if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
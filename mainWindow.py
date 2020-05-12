import tkinter as tk
from tkinter import ttk

from DataEntry import *
from Graphs import *

class Window():
    def __init__(self, master):
        self.master = master
        master.title("")
        master.minsize(1150, 850)
        
        self.dataFrame = ttk.LabelFrame(master, text = "Wprowadź dane")
        self.dataFrame.place(x = 5, y = 5, width = 300, height = 800)
        self.dataEntry = DataEntry(self.dataFrame)
        

        # tworzenie ramki do wyświetlania czy układ jest stabilny
        self.stabilityFrame = ttk.LabelFrame(self.dataFrame)
        self.stabilityFrame.pack(side="top", fill="x")
        self.stability_label = tk.Label(self.stabilityFrame, text = "Czy jest stabilny?", font = 20)
        self.stability_label.pack(fill="both", ipady = 5)
              
        # przycisk do wykreslenia wykresow
        self.draw_button = tk.Button(self.dataFrame, text = "Rysuj", font = 17, command = self.draw_function)
        self.draw_button.pack(side="top", fill="x", ipady = 5)

        self.drawFrame = ttk.LabelFrame(master, text = "Wykresy")
        self.drawFrame.place(x = 310, y = 5, width = 800, height = 800)

    def draw_function(self):
        self.impulse = self.dataEntry.get_impuls()
        self.impulse.wyswietl_wspolczynniki()

        if self.impulse.is_stable():
            self.stability_label.config(text = "STABILNY", compound = "center", foreground = "green")
        else:
            self.stability_label.config(text = "NIESTABILNY", compound = "center", foreground = "red")

        self.Graphs = Graphs(self.drawFrame, self.impulse)

        


if __name__ == "__main__":
    root = tk.Tk()
    app = Window(root)
    root.mainloop()
import tkinter as tk
from tkinter import ttk

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class Graphs:
    def __init__(self, drawFrame, impulse):
        self.drawFrame = drawFrame
        self.impulse = impulse

        self.tab_control = ttk.Notebook(self.drawFrame)

        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text = "Sygnał wejściowy")
        self.add_input_signal()

        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text = "")

        self.tab_control.pack(expan = 1, fill = "both")

        

        


    def add_input_signal(self):
        plt.ylabel("u(t)")
        plt.xlabel("t[ms]")
        plt.grid(True, which='both')
        plt.plot(self.impulse.time, self.impulse.signal_displayed)
        plt.show()

        f = Figure(figsize=(4,4), dpi=100)

        a = f.add_subplot(1,1,1)
        a.plot(self.impulse.time, self.impulse.signal_displayed)

        canvas = FigureCanvasTkAgg(f, self.tab1)
        canvas.get_tk_widget().pack(fill = "both", side = "bottom", expand = True)
        canvas._tkcanvas.pack(side = "top", fill = "both", expand = True)


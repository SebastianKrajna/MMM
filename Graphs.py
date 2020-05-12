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
        self.add_signal(self.impulse.time, self.impulse.input_singal, self.tab1)

        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text = "Sygnał wyjściowy")
        self.add_signal(self.impulse.time, self.impulse.output_signal, self.tab2)

        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab3, text = "Wykres amplitudowy")
        self.add_bode_amp()

        self.tab4 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab4, text = "Wykres częstotliwościowy")
        self.add_bode_phase()
        

        self.tab_control.pack(expan = 1, fill = "both")


    def add_signal(self, s_x, s_y, frame):
        f = Figure(figsize=(4,4), dpi=100)

        a = f.add_subplot(1,1,1)
        a.plot(s_x, s_y)

        a.set_ylabel("y")
        a.set_xlabel("x")

        canvas = FigureCanvasTkAgg(f, frame)
        canvas.get_tk_widget().pack(fill = "both", side = "bottom", expand = True)
        canvas._tkcanvas.pack(side = "top", fill = "both", expand = True)

    def add_bode_amp(self):
        fa = Figure(figsize=(4,4), dpi=100)

        aa = fa.add_subplot(1,1,1)
        aa.semilogx(self.impulse.w, self.impulse.wzm, color="blue", linewidth='1')

        aa.set_xlabel("Czestotliwosc")
        aa.set_ylabel("Wzmocnienie")

        canvas = FigureCanvasTkAgg(fa, self.tab3)
        canvas.get_tk_widget().pack(fill = "both", side = "bottom", expand = True)
        canvas._tkcanvas.pack(side = "top", fill = "both", expand = True)
    
    def add_bode_phase(self):
        fp = Figure(figsize=(4,4), dpi=100)

        ap = fp.add_subplot(1,1,1)
        ap.semilogx(self.impulse.w, self.impulse.faza, color="blue", linewidth='1')

        ap.set_xlabel("Czestotliwosc")
        ap.set_ylabel("Faza")

        canvas = FigureCanvasTkAgg(fp, self.tab4)
        canvas.get_tk_widget().pack(fill = "both", side = "bottom", expand = True)
        canvas._tkcanvas.pack(side = "top", fill = "both", expand = True)
   


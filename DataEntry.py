import tkinter as tk
from tkinter import ttk

# Klasa dla danych wejściowych
class DataEntry:
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame
        self.num_a = [tk.IntVar() for i in range(3)]
        self.num_b = [tk.IntVar() for i in range(4)]

        # inicializowanie wartosci poczatkowych
        self.num_a[0].set(0)
        self.num_a[1].set(0)
        self.num_a[2].set(0)
        self.num_b[0].set(0)
        self.num_b[1].set(0)
        self.num_b[2].set(0)
        self.num_b[3].set(0)

        # tworzenie ramki dla wspolczynnikow transmitancji
        self.dataFrame_wsp = ttk.LabelFrame(dataFrame)
        self.dataFrame_wsp.grid(column = 0, row = 0, sticky = "N", padx = 5, pady = 5, ipadx = 5, ipady = 5)
        
        # pola do wprowadzenia wspolczynnikow a 
        self.enter_a = []
        self.label_a = []
        for i in range(3):
            self.label_a.append(tk.Label(self.dataFrame_wsp, text = "a" + str(i) + " = "))
            self.label_a[i].grid(column = 0, row = i)
            self.enter_a.append(ttk.Entry(self.dataFrame_wsp, width = 6, textvariable = self.num_a[i]))
            self.enter_a[i].grid(column = 1, row = i)
            self.clear_entry_function(self.enter_a[i])
        
        # pola do wprowadzenia wspolczynnikow b 
        self.enter_b = []
        self.label_b = []
        for i in range(4):
            self.label_b.append(tk.Label(self.dataFrame_wsp, text = "  b" + str(i) + " = "))
            self.label_b[i].grid(column = 3, row = i)
            self.enter_b.append(ttk.Entry(self.dataFrame_wsp, width = 6, textvariable = self.num_b[i]))
            self.enter_b[i].grid(column = 4, row = i)
            self.clear_entry_function(self.enter_b[i])
            
            
        # tworzenie ramki dla wyswietlania transmitancji
        self.transferFrame = ttk.LabelFrame(dataFrame)
        self.transferFrame.grid(column = 0, row = 1, sticky = "W", padx = 5, pady = 5, ipadx = 5, ipady = 5)

        self.transfer_text = [tk.StringVar() for i in range(3)]
        self.transfer_text[0] = " Y(s) = " + str(self.num_b[3].get()) + "*s^3 + " + str(self.num_b[2].get()) + "*s^2 + " + str(self.num_b[1].get()) + "*s + " + str(self.num_b[0].get())
        self.transfer_text[1] = "________________________________" 
        self.transfer_text[2] = " X(s) = s^3 + " + str(self.num_a[2].get()) + "*s^2 + " + str(self.num_a[1].get())
        self.transfer_text[2] += "*s + " + str(self.num_a[0].get())

        self.label0 = tk.Label(self.transferFrame, text = self.transfer_text[0])
        self.label0.grid(column = 0, row = 0)
        self.label1 = tk.Label(self.transferFrame, text = self.transfer_text[1])
        self.label1.grid(column = 0, row = 1)
        self.label2 = tk.Label(self.transferFrame, text = self.transfer_text[2])
        self.label2.grid(column = 0, row = 2)

        # testowe do usuniecia - jak sie kliknie w ramke a i b to zmienia cyferki w transframe
        self.dataFrame_wsp.bind("<Button-1>", self.transfer_text_actualization)

        # tworzenie ramki do wyswietlania wyboru pobudzenia
        self.impulsFrame = ttk.LabelFrame(dataFrame)
        self.impulsFrame.grid(column = 0, row = 2, sticky = "W", padx = 5, pady = 5, ipadx = 5, ipady = 5)

        self.radValues = tk.IntVar()
        self.rad1 = ttk.Radiobutton(self.impulsFrame, text = "Sygnał prostokątny", value = 1, variable = self.radValues, command = self.rad_event)
        self.rad1.grid(column = 0, row = 0, sticky = "w", columnspan = 3)

        self.rad2 = ttk.Radiobutton(self.impulsFrame, text = "Skok", value = 2, variable = self.radValues, command = self.rad_event)
        self.rad2.grid(column = 0, row = 1, sticky = "w", columnspan = 3)

        self.rad3 = ttk.Radiobutton(self.impulsFrame, text = "Sinusoida", value = 3, variable = self.radValues, command = self.rad_event)
        self.rad3.grid(column = 0, row = 2, sticky = "w", columnspan = 3)

        self.rad4 = ttk.Radiobutton(self.impulsFrame, text = "Sygnał trójkątny", value = 4, variable = self.radValues, command = self.rad_event)
        self.rad4.grid(column = 0, row = 3, sticky = "w", columnspan = 3)

    def rad_event(self):
        radSelected = self.radValues.get()

        if radSelected == 1:
            self.impulsFrame.config(background = "red")
        elif radSelected == 2:
            self.impulsFrame.configure(background = "green")
        elif radSelected == 3:
            self.impulsFrame.configure(background = "purple")
        elif radSelected == 4:
            self.impulsFrame.configure(background = "yellow")

        
    # czyszczenie po kliknieciu na okienko
    def clear_entry_function(self, a):
        def clear_entry(event):
            a.delete(0, tk.END)
        a.bind('<Button-1>', clear_entry)

    def transfer_text_actualization(self, event):
        print("WYWOLANO MNIE")
        self.label0.configure(text = " Y(s) = " + str(self.num_b[3].get()) + "*s^3 + " + str(self.num_b[2].get()) + "*s^2 + " + str(self.num_b[1].get()) + "*s + " + str(self.num_b[0].get()))
        self.label2.configure(text = " X(s) = s^3 + " + str(self.num_a[2].get()) + "*s^2 + " + str(self.num_a[1].get()) + "*s + " + str(self.num_a[0].get()))
      
import tkinter as tk
from tkinter import ttk

from Impuls import *

# Klasa dla danych wejściowych
class DataEntry:
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame

        self.num_a = [tk.StringVar(value='0') for i in range(3)]
        self.num_b = [tk.StringVar(value='0') for i in range(4)]

        # tworzenie ramki dla wspolczynnikow transmitancji
        self.dataFrame_wsp = ttk.LabelFrame(dataFrame)
        self.dataFrame_wsp.pack(side="top", fill="x")
        
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
        self.transferFrame.pack(side="top", fill="x")
        self.show_transfer()


        # testowe do usuniecia - jak sie kliknie w ramke a i b to zmienia cyferki w transframe
        self.dataFrame_wsp.bind("<Button-1>", self.transfer_text_actualization)


        # tworzenie ramki do wyswietlania wyboru pobudzenia
        self.impulsFrame = ttk.LabelFrame(dataFrame)
        self.impulsFrame.pack(side="top", fill="x")

        self.radValues = tk.IntVar()
        self.rad1 = ttk.Radiobutton(self.impulsFrame, text = "Sygnał prostokątny", value = 1, variable = self.radValues, command = self.rad_event)
        self.rad1.grid(column = 0, row = 0, sticky = "w", columnspan = 3)

        self.rad2 = ttk.Radiobutton(self.impulsFrame, text = "Skok", value = 2, variable = self.radValues, command = self.rad_event)
        self.rad2.grid(column = 0, row = 1, sticky = "w", columnspan = 3)

        self.rad3 = ttk.Radiobutton(self.impulsFrame, text = "Sinusoida", value = 3, variable = self.radValues, command = self.rad_event)
        self.rad3.grid(column = 0, row = 2, sticky = "w", columnspan = 3)

        self.rad4 = ttk.Radiobutton(self.impulsFrame, text = "Sygnał trójkątny", value = 4, variable = self.radValues, command = self.rad_event)
        self.rad4.grid(column = 0, row = 3, sticky = "w", columnspan = 3)


        # tworzenie ramki do wczytania amplitudy, okresu i czasu trwania
        self.amplitudeFrame = ttk.LabelFrame(dataFrame)
        self.amplitudeFrame.pack(side="top", fill="x")

        self.impuls_settings = {'amplitude':   tk.StringVar(value='0'),
                                'period':      tk.StringVar(value='0'),
                                'duration':    tk.StringVar(value='0'),
                                'fulfillment': tk.StringVar(value='0'),
                                'start':       tk.StringVar(value='0')}                    

        self.amplitude_label = tk.Label(self.amplitudeFrame, text="Amplituda: ")
        self.amplitude_label.grid(column = 0, row = 0, sticky = "e")
        self.amplitude_entry = tk.Entry(self.amplitudeFrame,
                                        textvariable = self.impuls_settings['amplitude'],
                                        state = 'disabled')
        self.amplitude_entry.grid(column = 1, row = 0)

        self.period_label = tk.Label(self.amplitudeFrame, text="Okres[s]: ")
        self.period_label.grid(column = 0, row = 1, sticky = "e")
        self.period_entry = tk.Entry(self.amplitudeFrame,
                                        textvariable = self.impuls_settings['period'],
                                        state = 'disabled')
        self.period_entry.grid(column = 1, row = 1)

        self.duration_label = tk.Label(self.amplitudeFrame, text="Czas trwania[s]: ")
        self.duration_label.grid(column = 0, row = 2, sticky = "e")
        self.duration_entry = tk.Entry(self.amplitudeFrame, 
                                        textvariable = self.impuls_settings['duration'],
                                        state = 'disabled')
        self.duration_entry.grid(column = 1, row = 2)

        self.fulfillment_label = tk.Label(self.amplitudeFrame, text="Wypełnienie: ")
        self.fulfillment_label.grid(column = 0, row = 3, sticky = "e")
        self.fulfillment_entry = tk.Entry(self.amplitudeFrame,
                                        textvariable = self.impuls_settings['fulfillment'],
                                        state = 'disabled')
        self.fulfillment_entry.grid(column = 1, row = 3)

        self.start_label = tk.Label(self.amplitudeFrame, text="Początek skoku: ")
        self.start_label.grid(column = 0, row = 4, sticky = "e")
        self.start_entry = tk.Entry(self.amplitudeFrame,
                                        textvariable = self.impuls_settings['start'],
                                        state = 'disabled')
        self.start_entry.grid(column = 1, row = 4)


    pobudzenie = None
    def rad_event(self):
        radSelected = self.radValues.get()

        if radSelected == 1:
            pobudzenie = Impuls(self.impulsFrame, self.num_a, self.num_b, self.impuls_settings)
            pobudzenie.wyswietl_wspolczynniki()

            self.amplitude_entry['state'] =     'normal'
            self.period_entry['state'] =        'normal'
            self.duration_entry['state'] =      'normal'
            self.fulfillment_entry['state'] =   'normal'
            self.start_entry['state'] =         'disabled'

        elif radSelected == 2:
            self.amplitude_entry['state'] =     'normal'
            self.period_entry['state'] =        'disabled'
            self.duration_entry['state'] =      'normal'
            self.fulfillment_entry['state'] =   'disabled'
            self.start_entry['state'] =         'normal'

        elif radSelected == 3:
            self.amplitude_entry['state'] =     'normal'
            self.period_entry['state'] =        'normal'
            self.duration_entry['state'] =      'normal'
            self.fulfillment_entry['state'] =   'disabled'
            self.start_entry['state'] =         'disabled'

        elif radSelected == 4:
            self.amplitude_entry['state'] =     'normal'
            self.period_entry['state'] =        'normal'
            self.duration_entry['state'] =      'normal'
            self.fulfillment_entry['state'] =   'disabled'
            self.start_entry['state'] =         'disabled'

    def show_transfer(self):
        self.transfer_text = [tk.StringVar() for i in range(3)]
        self.transfer_text[0] = str(self.num_b[3].get()) + "*s^3 + " + str(self.num_b[2].get()) + "*s^2 + " + str(self.num_b[1].get()) + "*s + " + str(self.num_b[0].get())
        self.transfer_text[1] = "——————————————" 
        self.transfer_text[2] = " s^3 + " + str(self.num_a[2].get()) + "*s^2 + " + str(self.num_a[1].get())
        self.transfer_text[2] += "*s + " + str(self.num_a[0].get())

        self.label_y = tk.Label(self.transferFrame, text = " Y(s) ")
        self.label_y.grid(column = 0, row = 0)
        self.label_y = tk.Label(self.transferFrame, text = " ——— ")
        self.label_y.grid(column = 0, row = 1)
        self.label_y = tk.Label(self.transferFrame, text = " X(s) ")
        self.label_y.grid(column = 0, row = 2)

        self.label_equals = tk.Label(self.transferFrame, text = " = ")
        self.label_equals.grid(column = 1, row = 1)

        self.label0 = tk.Label(self.transferFrame, text = self.transfer_text[0])
        self.label0.grid(column = 2, row = 0)
        self.label1 = tk.Label(self.transferFrame, text = self.transfer_text[1])
        self.label1.grid(column = 2, row = 1)
        self.label2 = tk.Label(self.transferFrame, text = self.transfer_text[2])
        self.label2.grid(column = 2, row = 2)

        
    # czyszczenie po kliknieciu na okienko
    def clear_entry_function(self, a):
        def clear_entry(event):
            a.delete(0, tk.END)
        a.bind('<Button-1>', clear_entry)

    def transfer_text_actualization(self, event):
        print("WYWOLANO MNIE")
        self.label0.configure(text = " Y(s) = " + str(self.num_b[3].get()) + "*s^3 + " + str(self.num_b[2].get()) + "*s^2 + " + str(self.num_b[1].get()) + "*s + " + str(self.num_b[0].get()))
        self.label2.configure(text = " X(s) = s^3 + " + str(self.num_a[2].get()) + "*s^2 + " + str(self.num_a[1].get()) + "*s + " + str(self.num_a[0].get()))
      
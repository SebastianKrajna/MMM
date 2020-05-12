import tkinter as tk
from tkinter import ttk

from Impuls import *

# Klasa dla danych wejściowych
class DataEntry:
    def __init__(self, dataFrame):
        self.dataFrame = dataFrame


        # tworzenie ramki dla wspolczynnikow transmitancji
        self.dataFrame_wsp = ttk.LabelFrame(dataFrame)
        self.dataFrame_wsp.pack(side="top", fill="x", ipady = 2)
        self.num_a = [tk.StringVar(value='0') for i in range(3)]
        self.num_b = [tk.StringVar(value='0') for i in range(4)]
        self.show_dataFrame_wsp()
            

        # tworzenie ramki dla wyswietlania transmitancji
        self.transferFrame = ttk.LabelFrame(dataFrame)
        self.transferFrame.pack(side="top", fill="x")
        self.show_transferFrame()


        # tworzenie ramki do wyswietlania wyboru pobudzenia
        self.impulsFrame = ttk.LabelFrame(dataFrame)
        self.impulsFrame.pack(side="top", fill="x")
        self.radValues = tk.IntVar()
        self.show_impulsFrame()     


        # tworzenie ramki do wczytania amplitudy, okresu i czasu trwania
        self.amplitudeFrame = ttk.LabelFrame(dataFrame)
        self.amplitudeFrame.pack(side="top", fill="x")

        self.impuls_settings = {'amplitude':   tk.StringVar(value='0'),
                                'period':      tk.StringVar(value='0'),
                                'duration':    tk.StringVar(value='0'),
                                'fulfillment': tk.StringVar(value='0'),
                                'start':       tk.StringVar(value='0')}                    

        self.show_amplitudeFrame()


    def get_impuls(self):
        return Impuls(self.impulsFrame, self.num_a, self.num_b, self.impuls_settings, self.radValues.get())

    # wyswietlanie okienek do wpisania wspolczynnikow
    def show_dataFrame_wsp(self):
        # pola do wprowadzenia wspolczynnikow a 
        self.empty_column1 = tk.Label(self.dataFrame_wsp, text = "       ")
        self.empty_column1.grid(column = 0, row = 0)
        self.enter_a = []
        self.label_a = []
        for i in range(3):
            self.label_a.append(tk.Label(self.dataFrame_wsp, text = "a" + str(i) + " = "))
            self.label_a[i].grid(column = 1, row = i, pady = 1)
            self.enter_a.append(ttk.Entry(self.dataFrame_wsp, width = 7, textvariable = self.num_a[i]))
            self.enter_a[i].grid(column = 2, row = i, pady = 1)
            self.clear_entry_function(self.enter_a[i])
        
        # pola do wprowadzenia wspolczynnikow b 
        self.enter_b = []
        self.label_b = []
        for i in range(4):
            self.label_b.append(tk.Label(self.dataFrame_wsp, text = "  b" + str(i) + " = "))
            self.label_b[i].grid(column = 3, row = i, pady = 1)
            self.enter_b.append(ttk.Entry(self.dataFrame_wsp, width = 7, textvariable = self.num_b[i]))
            self.enter_b[i].grid(column = 4, row = i, pady = 1)
            self.clear_entry_function(self.enter_b[i])

    # wyswietlania transmitancji
    def show_transferFrame(self):
        self.transfer_text = [tk.StringVar() for i in range(3)]
        self.transfer_text[0] = str(self.num_b[3].get()) + "*s^3 + " + str(self.num_b[2].get()) + "*s\u00b2 + " + str(self.num_b[1].get()) + "*s + " + str(self.num_b[0].get())
        self.transfer_text[1] = "————————————" 
        self.transfer_text[2] = " s^3 + " + str(self.num_a[2].get()) + "*s^2 + " + str(self.num_a[1].get())
        self.transfer_text[2] += "*s + " + str(self.num_a[0].get())

        self.label_y = tk.Label(self.transferFrame, text = " Y(s) ", font = 15)
        self.label_y.grid(column = 0, row = 0)
        self.label_y = tk.Label(self.transferFrame, text = " ———", font = 15)
        self.label_y.grid(column = 0, row = 1)
        self.label_y = tk.Label(self.transferFrame, text = " X(s) ", font = 15)
        self.label_y.grid(column = 0, row = 2)

        self.label_equals = tk.Label(self.transferFrame, text = " = ", font = 15)
        self.label_equals.grid(column = 1, row = 1)

        self.label0 = tk.Label(self.transferFrame, text = self.transfer_text[0], font = 15)
        self.label0.grid(column = 2, row = 0)
        self.label1 = tk.Label(self.transferFrame, text = self.transfer_text[1], font = 15)
        self.label1.grid(column = 2, row = 1)
        self.label2 = tk.Label(self.transferFrame, text = self.transfer_text[2], font = 15)
        self.label2.grid(column = 2, row = 2)
        self.transfer_text_actualization()

    # wyswietlanie okienek wpisywania ustawien sygnalu
    def show_amplitudeFrame(self):
        self.amplitude_label = tk.Label(self.amplitudeFrame, text="Amplituda: ")
        self.amplitude_label.grid(column = 0, row = 0, sticky = "e")
        self.amplitude_entry = tk.Entry(self.amplitudeFrame,
                                        textvariable = self.impuls_settings['amplitude'],
                                        state = 'disabled')
        self.amplitude_entry.grid(column = 1, row = 0)
        self.clear_entry_function(self.amplitude_entry)

        self.period_label = tk.Label(self.amplitudeFrame, text="Okres[s]: ")
        self.period_label.grid(column = 0, row = 1, sticky = "e")
        self.period_entry = tk.Entry(self.amplitudeFrame,
                                        textvariable = self.impuls_settings['period'],
                                        state = 'disabled')
        self.period_entry.grid(column = 1, row = 1)
        self.clear_entry_function(self.period_entry)

        self.duration_label = tk.Label(self.amplitudeFrame, text="Czas trwania[s]: ")
        self.duration_label.grid(column = 0, row = 2, sticky = "e")
        self.duration_entry = tk.Entry(self.amplitudeFrame, 
                                        textvariable = self.impuls_settings['duration'],
                                        state = 'disabled')
        self.duration_entry.grid(column = 1, row = 2)
        self.clear_entry_function(self.duration_entry)

        self.fulfillment_label = tk.Label(self.amplitudeFrame, text="Wypełnienie: ")
        self.fulfillment_label.grid(column = 0, row = 3, sticky = "e")
        self.fulfillment_entry = tk.Entry(self.amplitudeFrame,
                                        textvariable = self.impuls_settings['fulfillment'],
                                        state = 'disabled')
        self.fulfillment_entry.grid(column = 1, row = 3)
        self.clear_entry_function(self.fulfillment_entry)

        self.start_label = tk.Label(self.amplitudeFrame, text="Początek skoku: ")
        self.start_label.grid(column = 0, row = 4, sticky = "e")
        self.start_entry = tk.Entry(self.amplitudeFrame,
                                        textvariable = self.impuls_settings['start'],
                                        state = 'disabled')
        self.start_entry.grid(column = 1, row = 4)
        self.clear_entry_function(self.start_entry)
   
    # wyswietlanie wyboru pobudzenia
    def show_impulsFrame(self):
        self.rad1 = ttk.Radiobutton(self.impulsFrame, text = "Sygnał prostokątny", value = 1, variable = self.radValues, command = self.rad_event)
        self.rad1.grid(column = 0, row = 0, sticky = "w", columnspan = 3)

        self.rad2 = ttk.Radiobutton(self.impulsFrame, text = "Skok", value = 2, variable = self.radValues, command = self.rad_event)
        self.rad2.grid(column = 0, row = 1, sticky = "w", columnspan = 3)

        self.rad3 = ttk.Radiobutton(self.impulsFrame, text = "Sinusoida", value = 3, variable = self.radValues, command = self.rad_event)
        self.rad3.grid(column = 0, row = 2, sticky = "w", columnspan = 3)

        self.rad4 = ttk.Radiobutton(self.impulsFrame, text = "Sygnał trójkątny", value = 4, variable = self.radValues, command = self.rad_event)
        self.rad4.grid(column = 0, row = 3, sticky = "w", columnspan = 3)

    # funkcja do akcji po wybraniu opcji pobudzenia
    def rad_event(self):
        radSelected = self.radValues.get()

        if radSelected == 1: # prostokatny
            self.amplitude_entry['state'] =     'normal'
            self.period_entry['state'] =        'normal'
            self.duration_entry['state'] =      'normal'
            self.fulfillment_entry['state'] =   'normal'
            self.start_entry['state'] =         'disabled'

        elif radSelected == 2: # skok
            self.amplitude_entry['state'] =     'normal'
            self.period_entry['state'] =        'disabled'
            self.duration_entry['state'] =      'normal'
            self.fulfillment_entry['state'] =   'disabled'
            self.start_entry['state'] =         'normal'

        elif radSelected == 3: # sinusoida
            self.amplitude_entry['state'] =     'normal'
            self.period_entry['state'] =        'normal'
            self.duration_entry['state'] =      'normal'
            self.fulfillment_entry['state'] =   'disabled'
            self.start_entry['state'] =         'disabled'

        elif radSelected == 4: # trojkatny
            self.amplitude_entry['state'] =     'normal'
            self.period_entry['state'] =        'normal'
            self.duration_entry['state'] =      'normal'
            self.fulfillment_entry['state'] =   'disabled'
            self.start_entry['state'] =         'disabled'

    # czyszczenie po kliknieciu na okienko
    def clear_entry_function(self, a):
        def clear_entry(event):
            a.delete(0, tk.END)
        a.bind('<Button-1>', clear_entry)

    # aktualizacja wyswietlania wspolczynnikow transmitancji
    def transfer_text_actualization(self):
        self.label0.configure(text = str(self.num_b[3].get()) + "s\u00b3 + " + str(self.num_b[2].get()) + "s\u00b2 + " + str(self.num_b[1].get()) + "s + " + str(self.num_b[0].get()))
        self.label2.configure(text = "s\u00b3 + " + str(self.num_a[2].get()) + "s\u00b2 + " + str(self.num_a[1].get()) + "s + " + str(self.num_a[0].get()))
        self.label0.after(10, self.transfer_text_actualization)
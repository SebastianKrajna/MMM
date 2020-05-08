import tkinter as tk
from tkinter import ttk

class Impuls:
    def __init__(self, impulsFrame, num_a, num_b, settings):
        self.impulsFrame = impulsFrame

        self.a = self.convert(num_a)
        self.b = self.convert(num_b)
        self.sygnal = []
        self.czas = []
        self.settings = self.convert_dict(settings)

    def wyswietl_wspolczynniki(self):
        print("Oto lista wspolczynnikow a: ")
        print(self.a)
        print("Oto lista wspolczynnikow b: ")
        print(self.b)
        print("Ustawienia")
        print(self.settings['amplitude'])
        print(self.settings['period'])
        print(self.settings['duration'])
        print(self.settings['fulfillment'])
        print(self.settings['start'])

    # funkcja zwracajaca czy uklad jest stabilny 
    def is_stable(self):
        if any(self.a) < 0:
             print("Układ jest niestabilny")
             return False
        elif self.a[2] > 0 and self.a[2]*self.a[1] - self.a[0] > 0: 
            print("Układ jest stabilny")
            return True

    # funkcja konwertujaca StringVar to int
    def convert(self, num_x):
        a = []
        for x in num_x:
            if x.get().isnumeric():
                a.append(float(x.get()))
            else:
                a.append(0)
        return a

    # funkcja konwertujaca StringVar to int w słowniku
    def convert_dict(self, set):
        d = {}
        for k,v in set.items():
            if v.get().isnumeric():
                d[k] = float(v.get())
            else:
                d[k] = 0
        return d
    


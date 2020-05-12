import tkinter as tk
from tkinter import ttk
from scipy import signal
import math

class Impuls:
    def __init__(self, impulsFrame, num_a, num_b, settings, radSelected):
        self.impulsFrame = impulsFrame

        self.a = self.convert(num_a)
        self.b = self.convert(num_b)
        self.settings = self.convert_dict(settings)
        self.radSelected = radSelected

        self.signal_displayed = []
        self.time = [0]
        self.max_ab = max(self.a + self.b)

        self.calculations()




    

    def calculations(self):
        # wyznaczanie czasu
        sum = 0
        for _ in range(int(self.settings['duration'])*1000-1):
            sum += 0.001
            self.time.append(sum)

        if self.radSelected == 1: # prostokatny
            self.signal_displayed = [self.settings["amplitude"] * signal.square(2 * math.pi * (1 / self.settings["period"]) * i, 
                                     self.settings["fulfillment"] / 100.) for i in self.time]

        elif self.radSelected == 2: # skok
            self.signal_displayed = [self.settings["amplitude"] if i >= self.settings["start"] else 0 for i in self.time]

        elif self.radSelected == 3: # sinusoida
            self.signal_displayed = [self.settings["amplitude"] * math.sin(2 * math.pi * (1 / self.settings["period"]) * i) for i in self.time]

        elif self.radSelected == 4: # trojkatny
            self.signal_displayed = [2 * self.settings["amplitude"] * signal.square(2 * math.pi * (1 / self.settings["period"]) * i, 0.5) for i in self.time]
            self.signal_displayed = self.calkowanie(self.signal_displayed)

    def calkowanie(self, data):
        sum = 0
        integral = [0,0]
        for i in range(1,len(data)-1):
            sum += (data[i] + data[i+1]) * (self.time[i+1] - self.time[i])/ 2.
            integral.append(sum)
        return integral
    

    def odejmowanie(self, v2, v1, v0):
        wynik = [0]
        for i in range(len(self.signal_displayed)-1) :
            wynik.append(self.signal_displayed[i] - v2[i] - v1[i] - v0[i])
        return wynik


    def dodawanie(self, wyjscie, v3, v2, v1, v0):
        wynik = []
        for i in range(len(wyjscie)) :
            wynik.append(wyjscie[i] + v3[i] + v2[i] + v1[i] + v0[i])
        return wynik


    def mnozenie(self, p, v):
        wynik = []
        for i in range(len(v)) :
            wynik.append(p * v[i])
        return wynik


    def wzmocnienie(self, wejscie_czy_wyjscie, v):
        if wejscie_czy_wyjscie == 0 :
            for i in range(len(self.a)) :
                v[i] = self.mnozenie(self.a[i], v[i])
        else :
            for i in range(len(self.b)) :
                v[i] = self.mnozenie(self.b[i], v[i])
        return v

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

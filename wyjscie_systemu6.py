from matplotlib import pyplot as plt
from scipy import signal
import numpy as np
import math


class Model:
    a = []
    b = []
    sygnal = []
    czas = []


    def podaj_wspolczynniki(model) :
        model.a = []
        model.b = []
        print("""
                b3*s^3 + b2*s^2 + b1*s^1 + b0*
        G(s) = -----------------------------------
                 1*s^3 + a2*s^2 + a1*s^1 + a0

        """)
        for i in range(3) :
            model.a.append(float(input("Podaj a" + str(i) + ": ")))
        for i in range(4) :
            model.b.append(float(input("Podaj b" + str(i) + ": ")))


    def wyswietl_wspolczynniki(model):
        if any(model.a) and any(model.b) :
            print("Oto lista wspolczynnikow a: ")
            print(model.a)
            print("Oto lista wspolczynnikow b: ")
            print(model.b)


    def wejscie_systemu(model) :
        model.sygnal = []
        x = int(input("""
            Wybierz rodzaj sygnału wejściowego:
            [1] - Sygnał prostokątny
            [2] - Skok 
            [3] - Sinusoidę
            [4] - Sygnal trojkatny
            [5] - Wyjdz
            Podaj numer opcji: """))

        ustaw = {}
        if x == 1 :
            ustaw = {'amplituda' : 0,
                     'wypelnienie[%]': 0,
                     'okres[s]' : 0,
                     'czas trwania[s]' : 0}
        elif x == 2 :
            ustaw = {'amplituda' : 0,
                     'poczatek skoku[s]' : 0,
                     'czas trwania[s]' : 0}
        elif x == 3 :
            ustaw = {'amplituda' : 0,
                     'okres[s]' : 0,
                     'czas trwania[s]' : 0}
        elif x == 4 :
            ustaw = {'amplituda' : 0,
                     'okres[s]' : 0,
                     'czas trwania[s]' : 0}
        if x != 5 :
            print("\n")
            for wymaganie in ustaw :
                ustaw[wymaganie] = float(input("Podaj " + wymaganie + ": "))
            model.czas = np.linspace(0, ustaw["czas trwania[s]"], int(ustaw["czas trwania[s]"] * 1000.), endpoint=True)
            if x == 1 :
                model.sygnal = [ustaw["amplituda"] * signal.square(2 * np.pi * (1 / ustaw["okres[s]"]) * i,
                                                             ustaw["wypelnienie[%]"] / 100.) for i in model.czas]
            elif x == 2 :
                model.sygnal = [ustaw["amplituda"] if i >= ustaw["poczatek skoku[s]"] else 0 for i in model.czas]
            elif x == 3 :
                model.sygnal = [ustaw["amplituda"] * math.sin(2 * np.pi * (1 / ustaw["okres[s]"]) * i) for i in model.czas]
            elif x == 4 :
                model.sygnal = [2 * ustaw["amplituda"] * signal.square(2 * np.pi * (1 / ustaw["okres[s]"]) * i, 0.5) for i in model.czas]
                model.sygnal = model.calkowanie(model.sygnal)

            if str(input("Czy pokazac sygnal wejsciowy?[TAK/NIE]: ")).upper( ) == "TAK" :
                plt.ylabel("u(t)")
                plt.xlabel("t[s]")
                plt.grid(True, which='both')
                plt.plot(model.czas, model.sygnal)
                plt.show()
        else :
            pass


    def wyswietl_wejscie(model):
        if any(model.sygnal) :
            plt.ylabel("u(t)")
            plt.xlabel("t[ms]")
            plt.grid(True, which='both')
            plt.plot(model.czas, model.sygnal)
            plt.show( )
        else :
            print("Nie zdefiniowano jeszcze sygnału wejściowego.")


    def calkowanie(model, dane):
        suma = 0
        calka = []
        dx = model.czas[1] - model.czas[0]
        for i in range(len(dane) - 1):
            suma += (dane[i] + dane[i + 1]) * dx / 2
            calka.append(suma)
        calka.append(suma)
        return calka


    def odejmowanie(model, v2, v1, v0):
        wynik = []
        for i in range(len(model.sygnal)) :
            wynik.append(model.sygnal[i] - v2[i] - v1[i] - v0[i])
        return wynik


    def dodawanie(model, wyjscie, v3, v2, v1, v0):
        wynik = []
        for i in range(len(wyjscie)) :
            wynik.append(wyjscie[i] + v3[i] + v2[i] + v1[i] + v0[i])
        return wynik


    def mnozenie(model, p, v):
        wynik = []
        for i in range(len(v)) :
            wynik.append(p * v[i])
        return wynik


    def wzmocnienie(model, wejscie_czy_wyjscie, v):
        if wejscie_czy_wyjscie == 0 :
            for i in range(len(model.a)) :
                if model.a[i] != 1 : v[i] = model.mnozenie(model.a[i], v[i])
        else :
            for i in range(len(model.b)) :
                if model.b[i] != 1 : v[i] = model.mnozenie(model.b[i], v[i])
        return v


    def wyswietlanie(model, wyjscie, v) :
        if str(input("Czy pokazać sygnały na poszczególnych gałęziach?[TAK/NIE]: ")).upper( ) == "TAK" :
            i = len(v) - 1
            while i >= 0 :
                if i != 3 : v[i] = model.calkowanie(v[i + 1])
                plt.ylabel("v" + str(i))
                plt.xlabel("t[s]")
                plt.grid(True, which='both')
                plt.plot(model.czas, v[i])
                plt.show( )
                i -= 1

        v = model.wzmocnienie(1, v)
        wyjscie = model.dodawanie(wyjscie, v[3], v[2], v[1], v[0])
        plt.ylabel("wyjscie")
        plt.xlabel("t[s]")
        plt.grid(True, which='both')
        plt.plot(model.czas, wyjscie)
        plt.show( )


    def symuluj(model) :
        print(". . .")
        if any(model.sygnal) and any(model.a) and any(model.b):
            wyjscie = [0 for _ in range(len(model.sygnal))]
            v = [0, 0, 0, 0]
            v[3] = model.sygnal
            for _ in range(int(10 * len(model.czas) / 1000)) :
                v[2] = model.calkowanie(v[3])
                v[1] = model.calkowanie(v[2])
                v[0] = model.calkowanie(v[1])
                v = model.wzmocnienie(0, v)
                v[3] = model.odejmowanie(v[2], v[1], v[0])
            model.wyswietlanie(wyjscie, v)


    def bode(model) :
        if any(model.a) and any(model.b) :
            s1 = signal.lti(model.b, [1] + model.a)
            w, wzm, faza = signal.bode(s1)
            plt.semilogx(w, wzm, color="blue", linewidth="1")
            plt.grid(True, which='both')
            plt.xlabel("Czestotliwosc")
            plt.ylabel("Wzmocnienie")
            plt.show( )
            plt.semilogx(w, faza, color="red", linewidth="1.1")
            plt.grid(True, which='both')
            plt.xlabel("Czestotliwosc")
            plt.ylabel("Faza")
            plt.show( )
        else :
            print("Nie podano jeszcze współczynników.")


def menu():
    system = Model( )
    while (True) :
        x = input("""
            ---WITAJ W MENU---
        Jaką operację chcesz wykonać?

        [1] - Podać współczynniki a i b
        [2] - Pokaz wspolczynniki a i b
        [3] - Ustawić sygnał wejściowy
        [4] - Pokaż aktualne wejście systemu
        [5] - Pokaż wyjście systemu
        [6] - Wykreśl charakterystyki częstotliwościowe
        [7] - Wyjdź z programu

         Podaj numer opcji: """)
        if x == '1' :
            system.podaj_wspolczynniki( )
        elif x == '2' :
            system.wyswietl_wspolczynniki( )
        elif x == '3' :
            system.wejscie_systemu( )
        elif x == '4' :
            system.wyswietl_wejscie( )
        elif x == '5' :
            system.symuluj( )
        elif x == '6' :
            system.bode( )
        elif x == '7' : return 0


menu()

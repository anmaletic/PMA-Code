# Vježba 2:
# U ovoj vježbi je potrebno napraviti sljedeće:
# Kreirati sučelje u kojem se u tekstualnom polju može unijeti lista cjelobrojnih 
# vrijednosti
# Polje za unos ciljane vrijednosti
# Na sučelju se nalazi gumb Pokreni koji pokreće binarno pretraživanje unesene liste 
# cjelobrojnih vrijednosti te ispisuje odgovarajuću poruku korisniku (ovisno o tome je li lista 
# sortirana te postoji li ciljana vrijednost u listi ili ne).

import copy
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD

unos = ""
target = ""
poruka = ""


def TtkStyle():
    style = ttk.Style()
    style.theme_use("alt")
    style.configure("TButton", background = "#2b544a", activebackground="Yellow", relief="flat", foreground="White", font=("Arial", 11, BOLD))
    style.map("TButton", background=[("active", "#595959")])


def InitializeMainWindow():
    global unos, target, poruka

    root = tk.Tk()

    TtkStyle()

    root.title("Pretraživanje")
    root.geometry("400x220")
    root.configure(background="#363636")
    root.resizable(0,0)

    unos = tk.StringVar()
    target = tk.StringVar()
    poruka = tk.StringVar()

    labelLista = ttk.Label(root, padding="10 10 0 0", background="#363636", text="Unesite listu cijelih brojeva odvojenih zarezom:", font=("Arial", 12, BOLD), foreground="White")
    labelLista.grid(row=0, column=0, columnspan=5, sticky=tk.W)

    entryLista = ttk.Entry(width="53", textvariable=unos)
    entryLista.grid(row=1, column=0, columnspan=5, sticky=tk.W, padx=20, pady=10)
    
    labelSearch = ttk.Label(root, padding="10 0 0 0", background="#363636", text="Unesite traženu vrijednost:", font=("Arial", 12, BOLD), foreground="White")
    labelSearch.grid(row=2, column=0, columnspan=5, sticky=tk.W)

    entryValue = ttk.Entry(width="15", textvariable=target)
    entryValue.grid(row=2, column=4, padx=7)

    buttonPretrazi = ttk.Button(width="39", text="Pretraži", command=PretraziCommand)
    buttonPretrazi.grid(row=3, column=0, columnspan=5, sticky=tk.W, padx=20, pady=10)

    labelRezultat = ttk.Label(root, padding="10 0 0 0", background="#363636", text="Rezultat:", font=("Arial", 12, BOLD), foreground="White")
    labelRezultat.grid(row=4, column=0, columnspan=5, sticky=tk.W)

    labelPoruka = ttk.Label(root, padding="20 5 0 0", background="#363636", font=("Arial", 12, BOLD), foreground="White", textvariable=poruka)
    labelPoruka.grid(row=5, column=0, columnspan=5, sticky=tk.W)

    root.mainloop()


def PretraziCommand():
    global unos, target, poruka

    if len(unos.get()) == 0:
        poruka.set("Lista je prazna.")
    else:
        if len(target.get()) == 0:
            poruka.set("Nije upisana tražena vrijednost.")
        else:
            listaUnosa = unos.get().replace(" ", "").split(",")
            
            for i in range(len(listaUnosa)):
                listaUnosa[i] = int(listaUnosa[i])            
                
            listaUnosaSorted = copy.deepcopy(listaUnosa)
            listaUnosaSorted.sort()
        
            if listaUnosa == listaUnosaSorted:
                _low = 0
                _high = len(listaUnosa) -1
                _result = BinarySearch(listaUnosa, int(target.get()), _low, _high)

                if _result:
                    poruka.set("Postoji tražena vrijednost u listi.")
                else:
                    poruka.set("Ne postoji tražena vrijednost u listi.")
            else:
                poruka.set("Lista nije sortirana.")


def BinarySearch(lista, cilj, low, high):
    if low > high:
        return False
    else:
        median_index = (low + high) // 2

        if cilj == lista[median_index]:
            return True
        elif cilj < lista[median_index]:
            return BinarySearch(lista, cilj, low, median_index-1)
        else:
            return BinarySearch(lista, cilj, median_index+1, high)


def Main():
    InitializeMainWindow()


Main()
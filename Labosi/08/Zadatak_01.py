# Vježba 1:
# U ovoj vježbi je potrebno napraviti sljedeće:
# - Napisati funkciju brojiZnakove koja za ulazni parametar vraća broj znakova koji su predani
# - Kreirati sučelje koje će imati sljedeće elemente:
#   o tekstualno polje za unos željenog teksta
#   o polje za ispis broja znakova
#   o gumb Pokreni koji poziva funkciju brojiZnakove
#   o gumb Obriši koji briše sadržaj polja za ispis broja znakova

import tkinter as tk
from tkinter import ttk

UneseniText = ""
IspisaniText = ""

def InitializeMainWindow():
    global UneseniText, IspisaniText

    root = tk.Tk()
    root.title("Brojač znakova")
    root.geometry("300x100")

    frame = ttk.Frame(root, padding="10 10 10 10")
    frame.pack(fill=tk.BOTH, expand=True)

    UneseniText = tk.StringVar()
    IspisaniText = tk.StringVar()

    labelUnos = ttk.Label(frame, text="Novi unos:")
    labelUnos.place(x="15", y="0")

    textboxUnos = ttk.Entry(frame, width="37", textvariable=UneseniText)
    textboxUnos.place(x="15", y="20")

    textboxIspis = ttk.Entry(frame, width="3", textvariable=IspisaniText)
    textboxIspis.place(x="242", y="20")

    buttonPokreni = ttk.Button(frame, text="Pokreni", width="19", command=brojiZnakove)
    buttonPokreni.place(x="15", y="50")

    buttonIzbrisi = ttk.Button(frame, text="Obriši", width="19", command=izbrisiIspis)
    buttonIzbrisi.place(x="143", y="50")

    root.mainloop()


def brojiZnakove():
    global UneseniText, IspisaniText

    IspisaniText.set(len(UneseniText.get()))


def izbrisiIspis():
    IspisaniText.set("")


def Main():
    InitializeMainWindow()
    

Main()
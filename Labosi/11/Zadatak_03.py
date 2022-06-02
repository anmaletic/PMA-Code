# Vježba 3:
# U ovoj vježbi je cilj vježbati rad sa skokovitim pretraživanjem. Kreirajte ručno tekstualnu 
# datoteku datoteka.txt u koju spremite minimalno 16 cijelih brojeva u rasponu od 1 do 
# 100.
# Napišite program u Pythonu koji će raditi sljedeće:
# - tražiti od korisnik unos cijelog broja v_broj u rasponu od 10 do 90
# - provjeriti skokovitim pretraživanjem nalazi li se v_broj u datoteci datoteka.txt

import random as rnd
import math

def napraviDatoteku():
    lista = []
    while len(lista) < 24:
        num = rnd.randint(1, 100)
        if num not in lista:
            lista.append(num)
    lista.sort()

    with open("datoteka.txt", "w") as dat:
        for num in lista:
            dat.write(f"{num}\n")


def skokovitoPretrazivanje(trazeniElement:int):
    lista = []
    with open("datoteka.txt") as dat:
        for line in dat:
            lista.append(int(line.removesuffix("\n")))
    
    n = len(lista)
    skok = math.sqrt(n)
    
    prethodni = 0
    while lista[int(min(skok, n)-1)] < trazeniElement:
        prethodni = skok
        skok += math.sqrt(n)
        if(prethodni >= n):
            return False    # -1

    while lista[int(prethodni)] < trazeniElement:
        prethodni += 1

        if prethodni == min(skok, n):
            return False    # -1

    if lista[int(prethodni)] == trazeniElement:
        return True         #int(prethodni)

    return False            # -1



def main():
    unos = int(input("Unesite broj u rasponu 10-90: "))

    result = skokovitoPretrazivanje(trazeniElement=unos)
    print(result)

#napraviDatoteku()
main()
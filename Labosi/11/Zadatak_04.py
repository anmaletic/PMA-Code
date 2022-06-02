# Vježba 4:
# U ovoj vježbi je cilj vježbati rad sa eksponencijalnim pretraživanjem. Kreirajte ručno 
# tekstualnu datoteku datoteka.txt u koju spremite minimalno 16 cijelih brojeva u rasponu 
# od 1 do 100.
# Napišite program u Pythonu koji će raditi sljedeće:
# - tražiti od korisnik unos cijelog broja v_broj u rasponu od 10 do 90
# - provjeriti eksponencijalnim pretraživanjem nalazi li se v_broj u datoteci 
# datoteka.txt

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


def ekspPretrazivanje(trazeniElement:int):
    lista = []
    with open("datoteka.txt") as dat:
        for line in dat:
            lista.append(int(line.removesuffix("\n")))
    
    n = len(lista)

    if lista[0] == trazeniElement:
        return True
    
    i = 1
    while i < n and lista[i] <= trazeniElement:
        i = i*2

    return binPretrazivanje(lista, i//2, min(i,n), trazeniElement)

def binPretrazivanje(lista, left, right, trazeniElement):
    if right >= left:
        mid = left + (right-left)//2

        if lista[mid] == trazeniElement:
            return True
        
        if lista[mid] > trazeniElement:
            return binPretrazivanje(lista, left, mid-1, trazeniElement)
        
        return binPretrazivanje(lista, mid+1, right, trazeniElement)
    
    return False


def main():
    unos = int(input("Unesite broj u rasponu 10-90: "))

    result = ekspPretrazivanje(trazeniElement=unos)
    print(result)

#napraviDatoteku()
main()
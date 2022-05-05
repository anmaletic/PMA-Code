# Vježba 2:
# U ovoj vježbi je cilj vježbati backtracking algoritam te vježbati import odvojenih modula.
# U Python kodu kreirajte praznu listu cijelih brojeva back_lista. Listu popunite s deset
# slučajno generiranih cijelih brojeva. Potom backtracking tehnikom nađite najmanji cijeli broj 
# koji se može dodati u listu back_lista a koji zadovoljava uvjet da će zbroj cijelih brojeva 
# u listi back_lista s tim brojem biti prost broj. Funkciju za provjeru prostog broja nazvati 
# is_prost_broj i staviti u poseban modu koji je potrebno importirati u modul u kojem se 
# primjenjuje backtracking algoritam. Pronađeni broj dodati u listu back_lista, ispisati 
# sadržaj liste, sumu brojeva u listi.

import random as rnd
from sympy import isprime


def dodajBroj(_lista):
    broj = 1
    while True:
        rez = (broj + sum(_lista))
        if isprime(rez):            
            _lista.append(broj)

            print(sum(_lista))
            break
        else:
            broj += 1


def main():
    back_lista = []
    back_lista = [rnd.randint(0,1000) for i in range(10)]

    dodajBroj(back_lista)

    print(back_lista)


main()
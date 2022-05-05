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


def FindLowestNumber(_lista:list, broj = 1):
    if IsProst(broj + sum(_lista)):
        _lista.append(broj)
        return broj
    return FindLowestNumber(_lista, broj+1)


def IsProst(n:int):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def main():
    back_lista = []
    back_lista.extend(rnd.randint(0,100) for i in range(10))

    num = FindLowestNumber(back_lista)
    
    print(back_lista)
    print(num)


main()

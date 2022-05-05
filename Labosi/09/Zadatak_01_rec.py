# Vježba 1:
# U ovoj vježbi je cilj vježbati backtracking algoritam.
# U Python kodu kreirajte praznu listu cijelih brojeva back_lista. Listu popunite s deset
# slučajno generiranih cijelih brojeva. Potom backtracking tehnikom nađite najmanji cijeli broj 
# koji se može dodati u listu back_lista a koji zadovoljava uvjet da će zbroj cijelih brojeva 
# u listi back_lista s tim brojem biti djeljiv brojem 13. Taj broj dodati u listu back_lista, 
# ispisati sadržaj liste, sumu brojeva u listi i količnik dijeljenja sume brojeva u listi brojem 13.

import random as rnd


def FindLowestNumber(_lista:list, broj = 1):
    if (broj + sum(_lista)) % 13 == 0:
        _lista.append(broj)
        return broj
    return FindLowestNumber(_lista, broj+1)


def main():
    back_lista = []
    back_lista.extend(rnd.randint(0,100) for i in range(10))

    print(FindLowestNumber(back_lista))



main()
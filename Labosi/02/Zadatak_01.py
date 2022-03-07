# Vježba 1:
# Ova vježba ima za svrhu ponavljanje rada s funkcijama.
# ● Na predavanjima ste upoznali funkciju ispisVremena, koja je ispisivala sistemsko vrijeme u
# satima, minutama i sekundama. Funkciju treba uporabom ugrađene funkcije strftime (kratica
# od engl. string from time) unutar paketa time, tako da se ispiše vrijeme u formatu „sati:
# minute: sekunde “. npr. „21:05:25“.
# ● Doradite kôd tako da se ispiše i trenutni datum. npr. „14.10.2019 21:20:45“

from datetime import datetime as dt

def ispisVremena():
    vrijeme = dt.now()
    print(vrijeme.strftime("%H:%M:%S"))
    print(vrijeme.strftime("%d.%m.%Y %H:%M:%S"))


def main():
    ispisVremena()


main()
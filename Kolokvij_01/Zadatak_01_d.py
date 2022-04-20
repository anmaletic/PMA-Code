# d)    Deklarirajte praznu listu L. Generirajte slučajni cijeli broj b, koji predstavlja broj elemenata u listi. Broj 
#       b mora biti u rasponu od 4 do 15 (granice nisu uključene). (5 bodova)
#       Od korisnika tražite unos b cijelih brojeva u listu L. Brojevi u listi moraju biti u rasponu od 10 do 60 
#       (granice su uključene) i u listi nema ponavljanja vrijednosti. (15 bodova) U okviru ovog zadatka je 
#       potrebno kreirati i duboku kopiju liste L te pojasniti razliku plitke i duboke kopije 
#       liste. (10 bodova) Primjer: ako je vrijednost za broj b jednako 6, tada bi korisnik mogao u listu L 
#       unijeti vrijednosti L = [15, 22, 45,48,39,27].


import copy
import random as rnd


def main():
    L = []
    b = rnd.randint(5,14)
    i = 0

    print(f"Broj brojeva: {b}")

    while i < b:
        unos = int(input(f"Unesite {i+1} broj izmedu 10 i 60: "))

        if unos >= 10 and unos <= 60 and L.count(unos) == 0:
            L.append(unos)
            i += 1

    print(L)
    Ldc = copy.deepcopy(L)
    Ldc[0] = 23

    print(L)
    print(Ldc)


main()
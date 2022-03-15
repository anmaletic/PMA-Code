# 3.
# Neka je cijena knjige 125 kn, a troškovi dostave 15 kn. Ako se naruči više 20 ili više primjeraka,
# nakladnik odobrava rabat od 10% te su troškovi dostave 7 kn po primjerku. Ako se naruči 50 ili više
# primjeraka, nakladnik odobrava rabat od 15% te su troškovi dostave 5 kn po primjerku. Napisati
# funkciju getTrosak koja ima formalni parametar brojKnjiga a vraća ukupni trošak za toliki
# broj knjiga.


def getTrosak(knjigaBroj):
    knjigaCijena = 125
    knjigaDostava = 15

    if( knjigaBroj < 20 ):
        return knjigaBroj * (knjigaCijena + knjigaDostava)
    elif ( knjigaBroj < 50 ):
        knjigaCijena = knjigaCijena * 0.9
        knjigaDostava = 7
        return knjigaBroj * (knjigaCijena + knjigaDostava)
    else:
        knjigaCijena = knjigaCijena * 0.85
        knjigaDostava = 5
        return knjigaBroj * (knjigaCijena + knjigaDostava)


def main():
    broj = 50

    print(getTrosak(broj))


main()
# c)    Deklarirati i upotrijebiti korisnički definirani izuzetak KorisnickiIzuzetak. Napisati kôd koji će 
#       tražiti od korisnika unos cijelog broja. Ako uneseni broj nije djeljiv sa 17 treba aktivirati
#       KorisnickiIzuzetak i javiti poruku da uneseni broj mora biti djeljiv sa 17.


class KorisnickiIzuzetak(Exception):
    pass


def main():
    unos = int(input("Unesite broj: "))
    try:
        if unos % 17 != 0:       
            raise KorisnickiIzuzetak("Uneseni broj mora bit djeljiv sa 17!")
        else:
            print(f"Unos {unos} je djeljiv sa 17.")   
    except KorisnickiIzuzetak as e:
        print(e)


main()
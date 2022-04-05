# a)    Tražiti od korisnika da unese svoj OIB. Unos završava ako korisnik unese 11 znakova te ako su svi znakovi 
#       brojevi. Ispisati OIB.


def main():
    while True:
        oib = input("Unesite OIB: ")

        if len(oib) == 11 and oib.isdigit():         
            break
        else:
            print("Niste upisali točan OIB.")   
    print(f"OIB: {oib}")


main()
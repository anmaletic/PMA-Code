# Vježba 4:
# Šifra uputnice za liječnički pregled se sastoji od šifre ustanove, šifre pregleda, datuma rođenja pacijenta
# i inicijala pacijenta.
# Npr. za uputnicu „01A2101012000AA“:
# - 01 – šifra ustanove
# - A21 – šifra pregleda
# - 01012000 – datum rođenja pacijenta
# - AA – inicijali pacijenta.
# 1. Napisati funkciju koja provjerava da li je šifra uputnice ispravna i tom slučaju vraća 1, a u
# suprotnom vraća 0.
# 2. Napisati funkciju koja na kraj šifre uputnice dodaje šifru doktora koji je obavio pregled te vraća
# novu šifru. Npr. ako je pregled obavio doktor sa šifrom „123“ nova šifra za gornju uputnicu bi bila
# „01A2101012000AA123“.
# U glavnom programu testirati rad funkcija na način da ako je šifra uputnice ispravna onda se kreira nova
# šifra u suprotnom se ispisuje poruka o grešci.



def CheckSifra(p_uputnica:str):
    if ( p_uputnica[0:2].isdigit() and
         p_uputnica[2].isalpha() and
         p_uputnica[3:5].isdigit() and
         p_uputnica[5:13].isdigit() and
         p_uputnica[14:].isalpha() ):     

        return 1
    else:
        return 0
        

def main():
    uputnicaNova:str    
    uputnica = "01A2101012000AA"

    if(CheckSifra(uputnica)):
        uputnicaNova = uputnica + "123"
        print(uputnicaNova)
    else:
        print("Sifra uputnice nije ispravna.")

main()
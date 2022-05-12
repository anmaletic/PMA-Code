# Vježba 2:
# U ovoj vježbi je cilj vježbati rad s listama i rječnicima.
# Napišite program u Pythonu koji će raditi sljedeće:
# - od korisnika se traži unos cjelobrojnih vrijednosti za listu L1. Prilikom pokretanja 
# programa unijeti nekoliko duplih vrijednosti. Unos se prekida kada korisnik unese 
# vrijednost 77, i ta vrijednost se ne unosi u listu.
# - program ispisuje koliko ima duplih vrijednosti u listi L1 na način da ispiše vrijednost i 
# broj ponavljanja. Npr., ako se broj 5 ponavlja 2 puta a broj 4 tri puta potrebno je ispisati:
# Vrijednosti koje se ponavljaju su:
# broj 5 – 2 puta
# broj 4 – 3 puta
# - programski kreirati rječnik R1 stavljajući u njega vrijednosti liste L1 na način da su 
# vrijednosti liste L1 ključevi a broj ponavljanja vrijednosti je vrijednost u rječniku za 
# svaki ključ. Ako se neka vrijednost ne ponavlja, tada je vrijednost u rječniku za taj ključ 
# jednaka 0.
# - ispisati sadržaj liste L1 i rječnika R1



L1 = []
while True:
    unos = int(input("Unesite broj: "))
    if unos == 77:
        break
    L1.append(unos)

rj = {}

for item in L1:
    if item not in rj.keys():
        counter = L1.count(item)

        if counter > 1:
            rj.update({item:counter})
        else:
            rj.update({item:0})
        
        print(item, ":", counter)

print(rj)

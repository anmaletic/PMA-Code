# Vježba 1:
# U ovoj vježbi je cilj vježbati rad s listama i skupovima.
# Napišite program u Pythonu koji će raditi sljedeće:
# - od korisnika se traži unos cjelobrojnih vrijednosti za listu L1. Prilikom pokretanja 
# programa unijeti nekoliko duplih vrijednosti. Unos se prekida kada korisnik unese 
# vrijednost 77, i ta vrijednost se ne unosi u listu.
# - program ispisuje koliko ima duplih vrijednosti u listi L1 na način da ispiše vrijednost i 
# broj ponavljanja. Npr., ako se broj 5 ponavlja 2 puta a broj 4 tri puta potrebno je ispisati:
# Vrijednosti koje se ponavljaju su:
# broj 5 – 2 puta
# broj 4 – 3 puta
# - programski kreirati skup S1 stavljajući u njega vrijednosti liste L1
# - pokazati ispisom sadržaja da S1 ne sadrži duple vrijednost


L1 = []
while True:
    unos = int(input("Unesite broj: "))
    if unos == 77:
        break
    L1.append(unos)

S1 = set(L1)

for item in S1:
    counter = L1.count(item)
    if counter > 1:
        print(item, ":", counter)

print(L1)
print(S1)


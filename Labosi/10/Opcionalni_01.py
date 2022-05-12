# Opcionalni zadatak 1:
# U ovoj vježbi je cilj vježbati rad s rječnicima.
# Napišite program u Pythonu koji će raditi sljedeće:
# - Od korisnika se traži da unese vrijednosti za ključeve rječnika R1 koji su cijeli brojevi 
# od 1 do 10.
# - Vrijednosti koje korisnik unosi moraju biti jedinstvene (vrijednosti koje korisnik unosi 
# nisu bitne sve dok su jedinstvene i cjelobrojne)
# - Programski kreirati novi rječnik R2 na način da su vrijednosti iz rječnika R1 ključevi 
# za rječnik R2 a ključevi za rječnik R2 su vrijednosti iz rječnika R1.

R1 = {}
R2 = {}

for i in range(10):
    while True:
        unos = int(input(f"Unos {i+1}: "))
        if unos not in R1.values():
            R1.update({i+1:unos})
            break

lkeys = list(R1.keys())
lvals = list(R1.values())

for i in range(10):
    R2.update({lvals[i] : lkeys[i]})

print(R1)
print(R2)
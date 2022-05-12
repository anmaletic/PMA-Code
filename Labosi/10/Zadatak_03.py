# Vježba 3:
# U ovoj vježbi je cilj vježbati rad s rječnicima i skupovima.
# Napišite program u Pythonu koji će raditi sljedeće:
# - kreira se rječnik R1, koji kao ključeve ima cijele brojeve od 1 do 10 a vrijednosti za 
# svaki od ključeva unosi korisnik od kojeg se traži unos za svaki ključ
# - kreira se rječnik R2 koji ima pet cjelobrojnih ključeva iz raspona od 1 do 20 a koji se 
# generiraju slučajno. Vrijednosti za generirane ključeve također popunjava korisnik od 
# koga se to traži.
# - programski se naprave skupovi S1 (od R1) te S2 (od R2) te se napravi skup S3 koji je 
# unija skupova S1 i S2.
# - ispisuju se vrijednosti svih skupova i rječnika. Potrebno je znati pojasniti sve ispisane 
# vrijednosti

import random as rnd
R1 = {}
R2 = {}

for i in range(10):
    unos = int(input("Unesite broj: "))
    R1.update({i+1:unos})

for i in range(5):
    unos = int(input("Unesite broj: "))
    while True:
        key = rnd.randint(1,20)
        if key not in R2.keys():
            R2.update({key:unos})
            break

print(R1)
print(R2)

S1 = set(R1)
S2 = set(R2)
S3 = S1.union(S2)

print(S1)
print(S2)
print(S3)


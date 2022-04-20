# a)    Deklarirajte dvije varijable a i b te ih popunite slučajnim brojevima. Slučajni brojevi trebaju biti 
#       u rasponu od 2 do 5 (uključujući granice).
# b)    Deklarirajte dvije varijable m i n te ih popunite slučajnim brojevima. Slučajni brojevi trebaju biti 
#       u rasponu od 2 do 5 (uključujući granice).
# c)    Napisati funkciju koja će ponavljati korake u dijelu zadatka a) i b) sve dok nije ispunjen uvjet da 
#       je b = m
# d)    Tražiti od korisnika unos cijelih brojeva koji su elementi matrice A dimenzija axb te matrice B 
#       dimenzija mxn.
# e)    Napisati funkciju koja će pomnožiti matrice A i B. Nije potrebno provjeravati uvjet ulančanosti 
#       jer je on ispunjen dijelom d) zadatka.


import random

start = 2
end = 2

a = random.randint(start,end)
b = random.randint(start,end)


m = random.randint(start,end)
n = random.randint(start,end)


while b != m:
    b = random.randint(start,end)
    m = random.randint(start,end)


matA = []
for i in range(a):
    row = []
    for j in range(b):
        row.append(int(input("Unos: ")))
    matA.append(row)


matB = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input("Unos: ")))
    matB.append(row)


rez = []
for i in range(a):
    row = []
    for j in range(n):
        row.append(0)
    rez.append(row)

print(matA)
print(matB)

print(rez)

for i in range(a):
    for j in range(n):
        rezultat = 0
        for k in range(m):
            rezultat += matA[i][k] * matB[k][j]
        rez[i][j] = rezultat

print(rez)
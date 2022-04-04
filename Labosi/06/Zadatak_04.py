# Vježba 4:
# U ovoj vježbi je cilj vježbati rad s listama lista te ocijeniti složenost algoritma.
# Napišite program koji će od korisnika tražiti unos broja redaka i stupaca dvije matrice (matA
# i matB), generirati slučajne cjelobrojne vrijednosti kao elemente matrica te ispisati umnožak 
# matrica matA i matB u vidu matrice matC. Ispisati sve tri matrice. Obradite pažnju na 
# granične situacije (npr. kada nisu ispunjeni uvjeti za množenje matrica – ulančano pravilo).
# Koja je složenost primijenjenog algoritma množenja matrica?

import random as rnd


def IzradiMatricu(_row:int, _column:int):
    _matrix = []
    for i in range(_row):
        _matrix.append(list(rnd.randint(0, 10) for num in range(_column)))

    return _matrix


def main():
    # rowA = int(input("Unesite broj redaka matrice A : "))
    # colA = int(input("Unesite broj stupaca matrice A: "))

    # rowB = int(input("Unesite broj redaka matrice B : "))
    # colB = int(input("Unesite broj stupaca matrice B: "))

    # matricaA = IzradiMatricu(rowA, colA)
    # matricaB = IzradiMatricu(rowB, colB)
    matricaC = []

    rowA = 2
    rowB = 2
    colA = 2
    colB = 2

    matricaA = [[2,1], [1,0]]
    matricaB = [[-1,1], [5,2]]


    if colA == rowB:       
        for i in range(rowA):
            temp = []
            for j in range(colB):
                rez = 0
                for k in range(colA):
                    rez += matricaA[i][k] * matricaB[k][j]
                temp.append(rez)
            matricaC.append(temp)

    print(matricaA)
    print(matricaB)
    print(matricaC)



main()
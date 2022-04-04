from random import randint
import numpy as np


print('*INVERZNE MATRICE*')
print('******************\n')
print('0 = KRAJ PROGRAMA\n')

while True:
    redak = int(input('Unesite broj redaka matrice: '))
    if redak == 0:
        print('\n***KRAJ PROGRAMA***')
        break

    stupac = int(input('Unesite broj stupaca matrice: '))
    if stupac == 0:
        print('\n***KRAJ PROGRAMA***')
        break

    matrica = []
    for i in range(redak):
        st = []
        for j in range(stupac):
            st.append(randint(1,9))
        matrica.append(st)
    print('\nVaša matrica izgleda ovako:')
    for st in matrica:
        print(st)
    print()


    if redak != stupac:
        print('Ova matrica nema determinantu pa nema ni inverz')
    else:
        det = np.linalg.det(matrica)
        print('determinanta matrice je',round(det,2))

        if det == 0:
            print('\nOva matrica nema inverz!')
        else:
            inverz = np.linalg.inv(matrica)
            inverz = np.matrix.round(inverz, decimals= 2)

        print()
        print('INVERZ MATRICE:\n',inverz)

    print('\nNOVA MATRICA')
    print('************')
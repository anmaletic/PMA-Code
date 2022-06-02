# Vježba 3:
# U ovoj vježbi je cilj vježbati rad s Quick sort algoritmom.
# Napišite program u Pythonu koji će raditi sljedeće:
# o od korisnika se traži unos cjelobrojnih vrijednosti za listu L3. Unos se prekida 
# kada korisnik unese vrijednost 22, i ta se vrijednost unosi u listu.
# o kreirajte Python kod s implementacijom Quick sort algoritma nad vrijednostima 
# liste L3 i ispišite rezultat sortiranja. Pivot element odaberite random među 
# vrijednostima liste L3
# o kolika je složenost primijenjenog algoritma?
# o napišite ručne korake primjene Quick sort algoritma nad listom L3

import random as rnd

def QuickSort(lista:list, start, end):
    if start >= end:
        return

    pivotIndex = rnd.randrange(start, end+1)
    pivotElement = lista[pivotIndex]

    lista[end], lista[pivotIndex] = lista[pivotIndex], lista[end]

    lessThanPointer = start

    for i in range(start, end):
        if lista[i] < pivotElement:
            lista[i], lista[lessThanPointer] = lista[lessThanPointer], lista[i]

            lessThanPointer += 1
    lista[end], lista[lessThanPointer] = lista[lessThanPointer], lista[end]

    QuickSort(lista, start, lessThanPointer-1)
    QuickSort(lista, lessThanPointer+1, end)


def main():
    lista = []
    lista = [15, 56, 89, 45, 12, 65, 78, 45, 69, 12, 45, 2, 3, 74, 56, 22]

    # while  True:
    #     unos = int(input("Unesite broj: "))
    #     if unos == 22:
    #         break
    #     lista.append(unos)

    print(lista)

    QuickSort(lista, 0, len(lista)-1)
    
    print(lista)


main()
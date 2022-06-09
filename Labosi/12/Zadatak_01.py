# Vježba 1:
# U ovoj vježbi je cilj vježbati rad s Bubble sort algoritmom.
# Napišite program u Pythonu koji će raditi sljedeće:
# o od korisnika se traži unos cjelobrojnih vrijednosti za listu L1. Unos se prekida 
# kada korisnik unese vrijednost 44, i ta se vrijednost unosi u listu.
# o kreirajte Python kod s implementacijom Bubble sort algoritma nad 
# vrijednostima liste L1 i ispišite rezultat sortiranja
# o kolika je složenost primijenjenog algoritma?
# o napišite ručne korake primjene Bubble sort algoritma nad listom L1

def BubbleSortPythonic(lista:list):
    n = len(lista)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

def BubbleSortTemp(lista:list):
    count = 0
    n = len(lista)
    for i in range(n-1):
        for j in range(i+1, n):
            count += 1
            if lista[i] > lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
        print(lista)
    print(count)

def BubbleSort(lista:list):
    count = 0
    n = len(lista)
    for i in range(n):
        sorted = True
        for j in range(n-i-1):
            count += 1
            if lista[j] > lista[j+1]:
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
                sorted = False
        if sorted:
            break
    print(count)


def main():
    lista = []
    lista = [15, 56, 89, 45, 12, 65, 78, 45, 69, 12, 45, 2, 3, 74, 56, 44]

    # while 44 not in lista:
    #     unos = int(input("Unesite broj: "))
    #     lista.append(unos)

    print(lista)

    #BubbleSortPythonic(lista)
    BubbleSortTemp(lista)
    #BubbleSort(lista)
    
    print(lista)


main()
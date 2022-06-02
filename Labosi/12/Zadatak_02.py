# Vježba 2:
# U ovoj vježbi je cilj vježbati rad s Merge sort algoritmom.
# Napišite program u Pythonu koji će raditi sljedeće:
# o od korisnika se traži unos cjelobrojnih vrijednosti za listu L2. Unos se prekida 
# kada korisnik unese vrijednost 33, i ta se vrijednost ne unosi u listu.
# o kreirajte Python kod s implementacijom Merge sort algoritma nad vrijednostima 
# liste L2 i ispišite rezultat sortiranja
# o kolika je složenost primijenjenog algoritma?
# o napišite ručne korake primjene Merge sort algoritma nad listom L2




def MergeSort(lista:list):
    if len(lista) <= 1:
        return lista

    midIndex = len(lista)//2
    lSplit = lista[:midIndex]
    rSplit = lista[midIndex:]

    lSorted = MergeSort(lSplit)
    rSorted = MergeSort(rSplit)

    return Merge(lSorted, rSorted)
    
def Merge(left, right):
    result = []
    
    while (left and right):
        if left[0] < right[0]:
            result.append(left.pop(0))            
        else:
            result.append(right.pop(0))            
    
    if left:
        result += left
    if right:
        result += right

    return result

def main():
    lista = []
    lista = [15, 56, 89, 45, 12, 65, 78, 45, 69, 12, 45, 2, 3, 74, 56, 44]

    # while  True:
    #     unos = int(input("Unesite broj: "))
    #     if unos == 33:
    #         break
    #     lista.append(unos)

    print(lista)

    result = MergeSort(lista)
    
    print(result)


main()
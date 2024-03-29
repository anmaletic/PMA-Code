# Vježba 3:
# U ovoj vježbi je cilj vježbati izmjenu postojeće liste, pretraživanje određenih vrijednosti 
# unutar liste te ocijeniti složenost algoritma.
# Napišite Python kôd koji će čitati cjelobrojne vrijednosti koje unosi korisnik i spremajte ih u 
# listu. Neka 0 bude oznaka za kraj unosa. Napišite funkciju getJedinstvene koja vraća 
# jedinstvene vrijednosti u polaznoj listi. Dakle, mijenja se polazna lista – ne radi se nova 
# kopija liste.
# Npr., ako je korisnik unio vrijednosti [1,2,3,4,2,4,5] program treba vratiti listu [1,2,3,4,5].
# Koja je složenost algoritma koji ste primijenili?

from re import I


def getJedinstveneSetCast(lista:list):
    return list(set(lista))


def getJedinstveneSet(lista:list):
    helperSet = set()
    for num in lista:
        helperSet.add(num)
    lista = list(helperSet)
    return lista


def getJedinstvene(lista:list):
    tempList = []
    for num in lista:
        if num not in tempList:
            tempList.append(num)

    lista.reverse()
    for num in tempList:
        while lista.count(num) > 1:
            lista.remove(num)
    lista.reverse()
    return lista


def getJedinstveneContinue(lista:list):
    for i in range(len(lista)):
        j = i + 1
        while j < len(lista):
            if lista[i] == lista[j]:
                lista.pop(i)
                continue
            j += 1
    return lista


def main():
    listaBrojeva = []
    while True:
        unosBroj = int(input("Unesite broj: "))        
        
        if unosBroj != 0:
            listaBrojeva.append(unosBroj)
        else:
            break

    #print(getJedinstveneSet(listaBrojeva))
    #print(getJedinstvene(listaBrojeva))
    #print(getJedinstveneSetCast(listaBrojeva))
    print(getJedinstveneContinue(listaBrojeva))


main()
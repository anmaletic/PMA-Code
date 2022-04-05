# b)    Napišite Python kôd koji će čitati cjelobrojne vrijednosti koje unosi korisnik i spremajte ih u listu L. 
#       Neka broj dva (2) bude oznaka za kraj unosa. I broj 2 treba spremiti u listu. Nakon što su sve 
#       vrijednosti korisnika unesene u listu, ispišite ih pomoću funkcije getObratneParne (koju je 
#       potrebno kreirati) obrnutim redoslijedom ali da izuzmete neparne brojeve. 2 ne treba 
#       ispisivati. Vrijednosti ispišite jednu ispod druge. Koju složenost O ima algoritam koji ste 
#       implementirali?


def getObratneParne(lista:list):
    lista.reverse()
    for num in lista:
        if num % 2 != 0:
            lista.remove(num)
        else:
            if num != 2:
                print(num)


def main():
    L = []
    while L.count(2) == 0:
        unos = int(input("Unesite broj: "))
        L.append(unos)

    getObratneParne(L)


main()

# Slozenost algoritma je = 0(n)
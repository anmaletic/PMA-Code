# Vježba 2:
# U ovoj vježbi je cilj ponoviti operacije i ispravan način kopiranje liste, vježbati 
# pretraživanje određenih vrijednosti unutar liste te ocijeniti složenost algoritma.
# Napišite Python kôd koji će čitati cjelobrojne vrijednosti koje unosi korisnik i spremajte ih u 
# listu. Neka 0 bude oznaka za kraj unosa. Napišite funkciju makni getNajvece, a koja ima 
# ulazni parametar n te koja vraća novu kopiju liste iz koje je uklonjeno n najvećih 
# vrijednosti.
# Npr. ako je korisnik unio vrijednosti [2,17,45,9,56,44,89,8,1] a predano n=3, 
# program treba kreirati listu [2,17,9,44,8,1] jer su uklonjena tri člana s najvećim 
# vrijednostima: 89, 56, 45.
# Ako je korisnik unio vrijednosti [2,17,45,9,56,56,44,89,8,1] a predano n=3, 
# program treba kreirati listu [2,17,9,44,8,1] jer su uklonjena četiri (dva imaju istu
# vrijednost) člana s najvećim vrijednostima: 89,56,56,44.
# Koja je složenost algoritma koji ste primijenili?




def makniGetNajvece(lista:list, n:int):
    tempLista = list(lista)
    while n > 0:
        m = max(tempLista)
        try:
            while True:
                tempLista.remove(m)
        except:
            pass
        n -= 1       
    return tempLista


def main():
    listaBrojeva = []
    while True:
        unosBroj = int(input("Unesite broj: "))        
        
        if unosBroj != 0:
            listaBrojeva.append(unosBroj)
        else:
            break

    unosN = int(input("Koliko clanova zelite ukloniti: "))

    listaBrojevaNova = makniGetNajvece(listaBrojeva, unosN)
    print(listaBrojevaNova)
    

main()

#O(n)
# Vježba 5:
# U ovoj vježbi je cilj vježbati rad s brute-force pretraživanjem.
# Napišite program u Pythonu koji će raditi sljedeće:
# - kreirajte listu L koju će korisnik popuniti cijelim vrijednostima u rasponu od 50 do 500
# - unos vrijednosti staje kada korisnik unese broj 175 i taj broj ulazi u listu
# - pronaći tri elementa liste čiji je zbroj vrijednosti 1000
# - ispisati nađene brojeve te njihov zbroj. Ako nema brojeva koji zadovoljavaju uvjet treba 
# ispisati odgovarajuću poruku.
# Npr., ako su u listi vrijednosti [55, 85, 230, 420, 340, 485, 350, 175], program bi ispisao:
# Brojevi koji zadovoljavaju uvjet da im je zbroj 1000 su 230, 420, 350.


def BFPretrazivanje(lista:list):
    n = len(lista)
    for i in range(0, n-2):
        for j in range(1, n-1):
            for k in range(2, n):
                if lista[i] + lista[j] + lista[k] == 1000:
                    return lista[i], lista[j], lista[k]
    return ("Nemaaa")


def main():
    lista = [200, 500, 240, 420, 340, 485, 350, 300]
    result = BFPretrazivanje(lista)

    print(result)
    print(result[0]+result[1]+result[2])


main()               
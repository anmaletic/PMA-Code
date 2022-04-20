# Vježba 3:
# U ovoj vježbi je cilj vježbati osnovnu uporabu rekurzivne tehnike programiranja.
# Pomoću rekurzivne tehnike programiranja napisati funkciju mnozim_brojeve koja ima 
# ulazne parametre n i m a ispisuje vrijednosti n*m. Npr. ako se funkciji 
# printam_unatrag predaju aktualne vrijednost parametara 5 i 4, rezultat pokretanja 
# funkcije će biti 20.


def mnozim_brojeve(n, m):
    if n < m:
        return mnozim_brojeve(m, n)
    elif m != 0:
        return (n + mnozim_brojeve(n, m - 1))
    else:
        return 0

n = int(input('Unesi broj n: '))
m = int(input('Unesi broj m: '))
print(mnozim_brojeve(n, m))
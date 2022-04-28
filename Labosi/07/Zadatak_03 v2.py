# Vježba 3:
# U ovoj vježbi je cilj vježbati osnovnu uporabu rekurzivne tehnike programiranja.
# Pomoću rekurzivne tehnike programiranja napisati funkciju mnozim_brojeve koja ima 
# ulazne parametre n i m a ispisuje vrijednosti n*m. Npr. ako se funkciji 
# printam_unatrag predaju aktualne vrijednost parametara 5 i 4, rezultat pokretanja 
# funkcije će biti 20.


def mnozim_brojeve(m, n):
    if m == 0:
        return 0
    if n == 1:
        return m
 
    return m + mnozim_brojeve(m, n-1)

n = 4
m = 5
print(mnozim_brojeve(n, m))
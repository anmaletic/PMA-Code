# Vježba 4:
# U ovoj vježbi je cilj vježbati osnovnu uporabu rekurzivne tehnike programiranja.
# Pomoću rekurzivne tehnike programiranja napisati funkciju ispisujem_inverz koja 
# ima ulazni parametar s (predstavlja string) a ispisuje vrijednosti stringa s u inverznom 
# obliku. Npr. ako se funkciji ispisuje_inverz predaju aktualna vrijednost parametara 
# 'ovo je string' , rezultat pokretanja funkcije će biti 'gnirts ej ovo'.


def ispisujem_inverz(s:str):
    if len(s) == 1:
        print(s)
    else:
        print(s[-1], end="")
        ispisujem_inverz(s[:-1])

    
def ispisujem_inverz_prof(s:str):
    if len(s) <= 1:
        return s        
    return s[-1] + ispisujem_inverz_prof(s[:-1])


ispisujem_inverz("ovo je string")
print(ispisujem_inverz_prof("ovo je string"))
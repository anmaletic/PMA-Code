# Vježba 2:
# U ovoj vježbi je cilj vježbati osnovnu uporabu rekurzivne tehnike programiranja.
# Pomoću rekurzivne tehnike programiranja napisati funkciju printam_unatrag koja ima 
# ulazni parametar n a ispisuje vrijednosti od n do -n. Npr. ako se funkciji 
# printam_unatrag preda aktualna vrijednost parametra 5, rezultat pokretanja funkcije će 
# biti 5,4,3,2,1,0,-1,-2,-3,-4,-5.


def printam_unatrag(n, firstRun = True, _base = 0) -> int:    
    if firstRun:
        _base = -n
    
    if n == _base:
        print(n)
    else:
        print(n, end=" ")
        printam_unatrag(n-1, False, _base)

printam_unatrag(5)
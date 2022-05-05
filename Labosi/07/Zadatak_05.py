# Vježba 5:
# U ovoj vježbi je cilj vježbati osnovnu uporabu rekurzivne tehnike programiranja.
# Pomoću rekurzivne tehnike programiranja napisati funkciju crtam_zvjezdice koja 
# iscrtava zvjezdice (zadatak s I kolokvija).


def crtam_zvjezdice(n, counter = 1):
    if n == 0:
        return
    else:        
        if counter <= n:
            print("*" * counter, end="")
            print()
            crtam_zvjezdice(n, counter+1)


def crtam_zvjezdice1(n):
    if n == 0:
        return
    if n == 1:
        print("*")
        return
    crtam_zvjezdice1(n-1)
    print("*" * n)        
        


#crtam_zvjezdice(5)
crtam_zvjezdice1(10)
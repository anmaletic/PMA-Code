# Vježba 3:
# Tražiti od korisnika unos jednog od ponuđenih gradova.
# Program treba ispisati trenutno vrijeme u Zagrebu te trenutno vrijeme za upisani grad na
# osnovu dostupnih informacija ispod u zadatku.
# Ukoliko se upisani grad ne nalazi na listi ponuđenih, tražiti korisnika ponovni unos.
# Ponuđeni gradovi:
# ● Los Angeles(-9h)
# ● New York(-6h)
# ● London(-1h)
# ● Pariz(0h)
# ● Moskva(+2h)
# ● Beijing(+7h)
# ● Tokio(+8)

#   odabir grada pomocu indexa

from datetime import datetime

class Grad():
    def __init__(self, p_grad, p_zona):
        self.grad = p_grad
        self.zona = p_zona


def FillGradData(p_gradovi:list):
    p_gradovi.append(Grad("Los Angeles", -9))
    p_gradovi.append(Grad("New York", -6))
    p_gradovi.append(Grad("London", -1))
    p_gradovi.append(Grad("Pariz", 0))
    p_gradovi.append(Grad("Moskva", +2))
    p_gradovi.append(Grad("Beijing", +7))
    p_gradovi.append(Grad("Tokio", +8))

    
def main():
    gradovi = []
    FillGradData(gradovi)

    print("Ponudeni gradovi: ")
    for i in range(len(gradovi)):
        print(f"{i+1}. {gradovi[i].grad}")


    while True:
        unosGrad = int(input("Odaberite redni broj grada: "))
        odabir = unosGrad - 1        

        if odabir >= 0 and unosGrad < len(gradovi):
            vrijeme_zg = datetime.now()        
            vrijeme_odabir = vrijeme_zg.replace(hour = vrijeme_zg.hour + gradovi[odabir].zona)

            print(f"Zagreb: {vrijeme_zg.strftime('%H:%M')}    {gradovi[odabir].grad}: {vrijeme_odabir.strftime('%H:%M')}")    
            break
            
        else:
            print("Nije odabran grad sa popisa! Pokušajte ponovo!")
            print()
            continue


main()
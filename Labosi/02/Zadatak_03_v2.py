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

#   odabir grada unosom imena grada

from datetime import datetime

class Grad():
    def __init__(self, p_grad, p_zona):
        self.grad = p_grad
        self.zona = p_zona

def Gradovi(p_grad:list):
    p_grad.append(Grad("Los Angeles", -9))
    p_grad.append(Grad("New York", -6))
    p_grad.append(Grad("London", -1))
    p_grad.append(Grad("Paris", 0))
    p_grad.append(Grad("Moskva", +2))
    p_grad.append(Grad("Bejing", +7))
    p_grad.append(Grad("Tokyo", +8))


def main():
    lista_gradova = []
    
    Gradovi(lista_gradova)
    while True:
        Unos_grad = input("Unesite željeni grad: ")    
        odabirGrad:Grad

        for grad in lista_gradova:
            if grad.grad == Unos_grad:
                odabirGrad = grad
                break
        else:
            print("Nije odabran grad sa popisa! Pokušajte ponovo!")
            print()
            continue

        vrijeme_zg = datetime.now()
        vrijeme_odabir = vrijeme_zg.replace(hour = vrijeme_zg.hour + odabirGrad.zona)
        print(f"Zagreb: {vrijeme_zg.strftime('%H:%M')}    {odabirGrad.grad}: {vrijeme_odabir.strftime('%H:%M')}")
        break

    
main()
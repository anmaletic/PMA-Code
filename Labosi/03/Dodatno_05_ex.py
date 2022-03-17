# 5.
# Napisati definiciju klase Krug ako klasa Krug ima atribute srediste i polumjer. Kreirajte
# dvije instance klase Krug, maliKrug i velikiKrug. maliKrug ima srediste u točki (100, 100) i
# polumjer 80, a velikiKrug ima središte u točki (120,120) i polumjer 90. Kreirati Python kôd koji
# će provjeriti koja od dvije instance ima veću površinu te ispiše tu informaciju.

# Ovaj zadatak je proširenje zadatka 5 ove vježbe, s liste zadataka za dodatno vježbanje za I kolokvij.
# Potrebno je za predanu vrijednost točaka koje smo predali testnom Python kôdu provjeravati ako je predana
# točka na rubu neke od dvije instance klase Krug.


import math

class Krug(object):
    def __init__(self, p_srediste, p_polumjer) -> None:
        self.srediste = p_srediste
        self.polumjer = p_polumjer

    def Povrsina(self):
        return self.polumjer**2 * math.pi


def getRadius(p_tocka, p_krug:Krug):    
    Tx = p_tocka[0]
    Ty = p_tocka[1]

    Sx = p_krug.srediste[0]
    Sy = p_krug.srediste[1]

    r = p_krug.polumjer

    r1 = round(math.sqrt(((Tx-Sx)**2 + (Ty-Sy)**2)), 2)

    return r == r1

 
def main():
    maliKrug = Krug((100, 100), 80)
    velikiKrug = Krug((120, 120), 90)

    if(maliKrug.Povrsina() > velikiKrug.Povrsina()):
        print("maliKrug ima vecu povrsinu.")
    else:
        print("velikiKrug ima vecu povrsinu.")

    listaTocaka = [(100, 180), (144.19, 33.31), (120, 210), (33.31, 144.19), (30, 92), (200, 100)]

    for tocka in listaTocaka:
        if(getRadius(tocka, maliKrug)):
            print(f"Tocka {tocka} je na rubu malog kruga.")
        else:
            print(f"Tocka {tocka} nije na rubu malog kruga.")

        if(getRadius(tocka, velikiKrug)):
            print(f"Tocka {tocka} je na rubu velikog kruga.")
        else:
            print(f"Tocka {tocka} nije na rubu velikog kruga.")       
        
        print()


main()
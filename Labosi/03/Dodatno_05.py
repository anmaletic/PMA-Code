# 5.
# Napisati definiciju klase Krug ako klasa Krug ima atribute srediste i polumjer. Kreirajte
# dvije instance klase Krug, maliKrug i velikiKrug. maliKrug ima srediste u točki (100, 100) i
# polumjer 80, a velikiKrug ima središte u točki (120,120) i polumjer 90. Kreirati Python kôd koji
# će provjeriti koja od dvije instance ima veću površinu te ispiše tu informaciju.
import math

class Krug(object):
    def __init__(self, p_srediste, p_polumjer) -> None:
        self.srediste = p_srediste
        self.polumjer = p_polumjer

    def Povrsina(self):
        #rez = (self.polumjer^2) * math.pi 
        rez = self.polumjer**2 * math.pi
        print(rez)
        return rez


def main():
    maliKrug = Krug((100, 100), 80)
    velikiKrug = Krug((120, 120), 90)

    if(maliKrug.Povrsina() > velikiKrug.Povrsina()):
        print("maliKrug ima vecu povrsinu.")
    else:
        print("velikiKrug ima vecu povrsinu.")

main()
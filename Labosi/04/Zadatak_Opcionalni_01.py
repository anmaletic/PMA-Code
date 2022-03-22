# Opcionalni zadatak:
# Ovaj zadatak je opcionalan za rješavanje. Njegovo rješavanje će asistent uzeti u obzir kao
# dodatni plus u ocjeni laboratorijske vježbe. Ako zadatak ne riješite, to se neće uzeti u obzir za
# ocjenu laboratorijske vježbe. Rješavanjem opcionalnog zadatka možete dodatno poboljšati 
# svoje vještine rada u Python programskom jezike te Vam stoga sugeriramo da ga probate 
# riješiti.
# Neka klasa Covjek iz Vježbe 1 opisuje člana neke video-igrice u kojoj se događaju i 
# situacije u kojoj instanca klase bude eliminirana iz igrice. Napišite kod kojim će se proširiti 
# klasa Covjek a koji će sadržati metodu __del__ koja će eliminirati instancu klase 
# Covjek te __init__metodu koja će kreirati instancu klase Covjek. Kreirajte te uklonite 
# nekoliko instanci te pokažite koliko je ukupno kreirano instanci, koliko ih je uklonjeno te 
# koliko ih je još na aktivno. Pored poziva __del__ metode uključite i re-binding kao način 
# dereferenciranja instance objekta


class Covjek(object):
    _Created = 0
    _Active = 0
    _Deleted = 0
    _imeiprezime = "Pero Perić"

    def __init__(self) -> None:
        Covjek._Created += 1
        Covjek._Active += 1

    def __del__(self):
        Covjek._Active -= 1
        Covjek._Deleted += 1

    def PrintStats():
        print (f"Created: {Covjek._Created} \nActive: {Covjek._Active} \nDeleted: {Covjek._Deleted}")


def main():
    osoba1 = Covjek()
    osoba2 = Covjek()
    osoba3 = Covjek()
    osoba4 = Covjek()
    osoba5 = Covjek()
    osoba6 = Covjek()

    osoba3 = ""
    osoba4 = osoba5

    Covjek.PrintStats()


main()




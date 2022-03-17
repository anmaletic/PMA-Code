# Kreiraje klasu Ruksak sa sljedećim metodama:
# a) __init__ koja inicijalizira atribut sadrzaj_Ruksaka na praznu listu.
# b) putIn koja uzima objekt i stavlja ga u sadržaj objekta Ruksak
# c) getOut koji uzima objekt iz instance tipa Ruksak
# d) __str__ koja vraća sadržaj objekta Ruksak u obliku znakovnog niza
# Testirajte kreirani kod na način da kreirate dvije instance CrveniRuksak i PlaviRuksak tipa
# Ruksak. Dodajte tri elementa u CrveniRuksak. Nakon toga sadržaj iz instance CrveniRuksak
# kopirajte u instancu PlaviRuksak. Ispišite sadržaj oba ruksaka.

class Ruksak():
    def __init__(self):
        self.sadrzaj_Ruksaka = []

    def putIn(self, item):
        self.sadrzaj_Ruksaka.append(item)

    def getOut(self, item):
        self.sadrzaj_Ruksaka.remove(item)

    def __str__(self) -> str:
        return ", ".join(self.sadrzaj_Ruksaka)


def main():
    CrveniRuksak = Ruksak()
    PlaviRuksak = Ruksak()

    CrveniRuksak.putIn("Biljeznica")
    CrveniRuksak.putIn("Knjiga")
    CrveniRuksak.putIn("Olovka")

    PlaviRuksak.sadrzaj_Ruksaka = CrveniRuksak.sadrzaj_Ruksaka

    print(CrveniRuksak)
    print(PlaviRuksak)

main()
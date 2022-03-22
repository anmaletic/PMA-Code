# Potrebno je:
# - proširiti klasu Covjek iz Vježbe 1 na način da joj se doda cjelobrojna statička 
# varijabla _id i inicijalizirati ju na 0
# - na ispravan način kreirati metodu __init__ kako bi se vrijednost varijable _id
# uvećavala za 1
# - napisati kôd koji će kreirati četiri instance klase Covjek te pokazati preko ispisa 
# stanja varijable _id da su kreirane četiri instance klase Covjek

class Covjek(object):
    _id = 0
    _imeiprezime = "Pero Perić"

    def __init__(self) -> None:
        Covjek._id += 1


def main():
    osoba1 = Covjek()
    osoba2 = Covjek()
    osoba3 = Covjek()
    osoba4 = Covjek()

    print(Covjek._id)


main()
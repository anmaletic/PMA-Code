# Kreirajte klasu Covjek te statičku varijablu klase Covjek koja ima naziv 
# _imeIprezime te ju inicijalizirajte na vrijednost 'Pero Perić'.
# Potrebno je:
# - napisati kôd koji će demonstrirati oba načina čitanja vrijednosti varijable 
# _imeIprezime
# - napisati kôd koji će demonstrirati oba načina pokušaja promjene varijable
# _imeIprezime. Objasnite u kako se razlikuju oba pristupa po pitanju postupka te po 
# pitanju rezultata.

class Covjek(object):
    _imeiprezime = "Pero Perić"


def PrintClass():
    print(Covjek._imeiprezime)


def PrintInstance():
    osoba = Covjek()
    print(osoba._imeiprezime)


def main():
    PrintClass()
    PrintInstance()


main()
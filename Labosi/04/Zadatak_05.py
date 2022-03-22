# Cilj vježbe je pokazati razumijevanje jednakosti objekata po ekvivalentnosti objekata po 
# sadržaju.
# Potrebno je:
# - kreirajte klasu Human koja ima varijablu _nameAndSurname te ju inicijalizirajte na 
# vrijednost 'Pero Perić'.
# - Prilagodite metodu __eq__ tako da osigurate da su objekti klasa Covjek i Human
# ekvivalentni ako su im vrijednosti varijabli _nameAndSurname te _imeIprezime
# jednake. Napišite kod koji će potvrditi ispravnost definirane ekvivalentnosti.


class Covjek(object):
    _imeiprezime = "Pero Perić"

    def __eq__(self, __o: object) -> bool:
        return self._imeiprezime == __o._nameAndSurname


class Human(object):
    _nameAndSurname = "Pero Perić"

    def __eq__(self, __o: object) -> bool:
        return  self._nameAndSurname == __o._imeiprezime


def main():
    osoba = Covjek()
    person = Human()
    print(osoba == person)
    print(person == osoba)
    

main()
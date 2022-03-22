# Cilj vježbe je pokazati razumijevanje jednakosti objekata po identitetu i ekvivalentnosti 
# objekata po sadržaju.
# Potrebno je:
# - na primjeru klase Covjek iz Vježbe 1, Vježbe 2 i Vježbe 3 napišite kôd u kojem 
# kreirajte dvije referentne varijable tipa Covjek i odgovarajući broj instanci kako biste 
# pokazali jednakost objekata. Pokažite preko odgovarajuće jednakosti da se radi o 
# istom objektu te i preko vrijednosti varijable _imeIprezime.


class Covjek(object):
    _imeiprezime = "Pero Perić"


def main():
    osoba1 = Covjek()
    osoba2 = Covjek()
    osoba1 = osoba2

    print(osoba1 == osoba2)
    print(osoba1._imeiprezime == osoba2._imeiprezime)


main()
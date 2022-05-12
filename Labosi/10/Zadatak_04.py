# Vježba 4:
# U ovoj vježbi je cilj vježbati rad s n-torkama i iteratorima.
# Napišite program u Pythonu koji će raditi sljedeće:
# - od korisnika se traži unos pet string vrijednosti za n-torku vrsteVoca
# - nakon ispravnog unosa je potrebno uporabom funkcija next ispisati unesene vrijednosti 
# u n-torku.
# - napisati i dio kôda koji provjerava i ispisuje tip iteratora te n-torke vrsteVoca.



lista = [input("Voce: ") for i in range(5)]
vrsteVoca = tuple(lista)

it = iter(vrsteVoca)
print(type(it))


try:
    while True:
        i = next(it)
        print(i)
except StopIteration:
    pass
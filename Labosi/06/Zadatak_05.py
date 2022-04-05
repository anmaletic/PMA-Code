# Vježba 5:
# U ovoj vježbi je cilj vježbati rad s jednostruko povezanim listama.
# Na osnovu koda koji ste upoznali tijekom predavanja i auditornih vježbi kreirajte dvije 
# instance klase jednostruko povezane liste. Neka se varijable instance zovu 
# prvaJPovezanaLista i drugaJPovezanaLista. Osmislite algoritam koji će spojiti 
# te dvije liste u jednu. Kao parametre treba predati reference na prvi čvor obje liste. Liste treba 
# spojiti tako da se na kraj elemenata prve liste prvaJPovezanaLista dodaju svi elementi 
# druge liste drugaJPovezanaLista. Napisati kod za testiranje programa.


class Empty(Exception):
    """Pogreška zbog pokušaja pristupu elementu iz praznog containera"""
    pass


class LinkedStack:

    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next) -> None:
            self._element = element
            self._next = next

        
def main():
    prvaJpovezanaLista = LinkedStack()
    drugaJpovezanaLista = LinkedStack()
    



    print(prvaJpovezanaLista)
    print(drugaJpovezanaLista)
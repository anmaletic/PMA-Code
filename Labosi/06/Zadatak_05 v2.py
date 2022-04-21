# Vježba 5:
# U ovoj vježbi je cilj vježbati rad s jednostruko povezanim listama.
# Na osnovu koda koji ste upoznali tijekom predavanja i auditornih vježbi kreirajte dvije 
# instance klase jednostruko povezane liste. Neka se varijable instance zovu 
# prvaJPovezanaLista i drugaJPovezanaLista. Osmislite algoritam koji će spojiti 
# te dvije liste u jednu. Kao parametre treba predati reference na prvi čvor obje liste. Liste treba 
# spojiti tako da se na kraj elemenata prve liste prvaJPovezanaLista dodaju svi elementi 
# druge liste drugaJPovezanaLista. Napisati kod za testiranje programa.


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.FN = None

    def append(self, value):
        newNode = Node(value)
        if self.FN == None:   
            self.FN = newNode        
        else:
            cN = self.FN
            while cN.next != None:
                cN = cN.next
            cN.next = newNode
          
    def __str__(self) -> str:
        value = ""
        if self.FN is None:
            return value
        cN = self.FN
        while cN != None:
            value += str(cN.value) + ", "
            cN = cN.next
        return value

        
def main():
    sll = LinkedList()
    sll.append(6)
    sll.append(1)
    sll.append(2)
    sll.append(8)

    print(sll)

    temp = ""


main()
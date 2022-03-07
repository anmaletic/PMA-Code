# Vježba 7:
# Kreirati klasu ListaBrojeva koja ima sljedeće metode:
# a) __init__ koja prima listu brojeva
# b) uvecaj(x:int) koja svaki broj u listi uvećava za x i vraća novu listu
# c) umanji(x:int) koja svaki broj u listi umanjuje za x i vraća novu listu
# d) parni() koja vraća listu samo parnih brojeva iz predane liste
# e) neparni() koja vraća listu samo neparnih brojeva iz predane liste
# f) djeljiviSa(x:int) koja vraća listu brojeva koji su djeljivi sa x
# g) promjeniListuBrojeva(novaListaBrojeva:list) koja prima novu listu brojeva te se prethodna
# lista zamjenjuje sa novom

class ListaBrojeva():
    def __init__(self, p_lista:list):
        self.lista = p_lista

    def uvecaj(self, x:int):
        for broj in self.lista:
            broj += x

    def umanji(self, x:int):
        for broj in self.lista:
            broj -= x

    def parni(self):
        lista_temp = []
        for broj in self.lista:
            if broj % 2 == 0:
                lista_temp.append(broj)
        return lista_temp

    def neparni(self):
        lista_temp = []
        for broj in self.lista:
            if broj % 2 != 0:
                lista_temp.append(broj)
        return lista_temp

    def djeljiviSa(self, x:int):
        lista_temp = []
        for broj in self.lista:
            if broj % x == 0:
                lista_temp.append(broj)
        return lista_temp

    def promjeniListuBrojeva(self, novaListaBrojeva:list):
        self.lista = novaListaBrojeva

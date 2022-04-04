import random as rnd
import time


def RemoveNajvecihN(lista:list, n:int):
    lista.sort(reverse=True)
    while n > 0:
        # if(lista[0] == lista[1]):
        #     lista.remove(lista[0])
        # else:
        #     lista.remove(lista[0])
        #     n -= 1

        lista.remove(lista[0])
        if(lista[0] != lista[1]):
            n -= 1

    return lista


def RemoveNajvecihNComp(lista:list, n:int):
    lista.sort(reverse=True)
    while n > 0:
        temp = lista[0]
        lista = [i for i in lista if i != temp]
        n -= 1
       
    return lista


def RemoveNajvecihNMax(lista:list, n:int):
    while n > 0:
        m = max(lista)
        c = lista.count(m)
        try:
            while True:
                lista.remove(m)
        except:
            pass
        n -= 1

    return lista


def randomLista(n, f):
    '''funkcija pravi listu n random brojeva do f'''
    lista = list(rnd.randint(1,f) for i in range(n))
    return lista
    
    
def main():
    lista = randomLista(200000,5000)

    start = time.time()
    RemoveNajvecihN(lista, 200)
    end = time.time()
    print('%4f'%(end-start))
    temp = ""


main()
import random as rnd
import time

def makniGetNajvece(lista:list, n):
    for i in range(n):
        if lista.count(max(lista)) > 1:
            for j in range (lista.count(max(lista))):
                lista.remove(max(lista))
        else:
            lista.remove(max(lista))
    return lista


def makniGetNajvece2(lista:list, n):
    b = 0
    while b < n:
        if lista.count(max(lista)) > 1:
            lista.remove(max(lista))
            continue
        else:
            lista.remove(max(lista))
            b += 1
    return lista


def makniGetNajvece3(lista:list, n:int):
    lista.sort(reverse=True)
    while n > 0:
        if(lista[0] == lista[1]):
            lista.remove(lista[0])
        else:
            lista.remove(lista[0])
            n -= 1
       
    return lista


def makniGetNajvece4(lista:list, n:int):
    while n > 0:
        m = max(lista)
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
lista1 = randomLista(100000, 2000)    
lista2 = list(lista1)
lista3 = list(lista1)
lista4 = list(lista1)
lista5 = list(lista1)

nBrojeva = 100
   
start = time.time()
test1 = makniGetNajvece(lista1, nBrojeva)
end = time.time()
print('%4f'%(end-start))

start = time.time()
test2 = makniGetNajvece2(lista2, nBrojeva)
end = time.time()
print('%4f'%(end-start))

start = time.time()
test3 = makniGetNajvece3(lista3, nBrojeva)
end = time.time()
print('%4f'%(end-start))

start = time.time()
test4 = makniGetNajvece4(lista4, nBrojeva)
end = time.time()
print('%4f'%(end-start))
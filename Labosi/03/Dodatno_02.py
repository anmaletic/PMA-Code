# 2. 
# Napisi funkciju ispisiNtiPrim koja će imati formalni parametar redniBroj cjelobrojen
# vrijednosti. Funkcija vraća n-ti prosti broj. Npr. ako smo predali vrijednost 3, funkcija vraća
# vrijednost 5 jer je na popisu prostih brojeva 2,3,5,7,11 .. broj 5 treći broj u slijedu. Smatramo da broj
# 1 nije ni prosti ni složeni broj te je broj 2 prvi prosti broj.

def ispisiNtiPrim(p_n):    
    num = 2
    prims = []
    while len(prims) < 5:
        djeliteljiCount = 0
        for i in range(2,num):
            if num % i == 0:
                djeliteljiCount += 1

        if(djeliteljiCount == 0):
            prims.append(num)
            
        num += 1
    return prims[p_n-1]


def main():
    n = 3
    print(ispisiNtiPrim(n))


main()
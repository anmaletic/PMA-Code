# 1. 
# Napisati funkciju ispisiPrim koja će ispisati prvih 5 prostih brojeva.

def ispisiPrim():    
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
    return prims


def main():
    print(ispisiPrim())


main()
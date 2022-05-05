# Opcionalni zadatak 1:
# Napišite primjer Python kôda koji ispisuje broj cijelih brojeva unutar tekstualne datoteke.
# Npr. za sljedeću datoteku


def BrojiCijele():
    with open("testna3.txt") as dat:
        count = 0
        temp = dat.read()
        for znak in temp:
            if znak.isdigit():
                count += 1
        print(count)

    
def main():
    BrojiCijele()


main()
# Vježba 4:
# U ovoj vježbi je cilj vježbati uporabu cijelih i decimalnih brojeva s tekstualnim datotekama.
# Budući metoda write prima kao argument znakovni niz, demonstrirati kako se u datoteku 
# insertiraju cjelobrojne i decimalne vrijednosti. Potrebno je demonstrirati uporabu metode str
# te pomoću operatora formatiranja (malo istražite ovu opciju).

def AddToFile(_value):
    with open("testna1.txt", "a", encoding="UTF-8") as dat:
        dat.write(str(_value) +"\n")
        dat.write(f"{_value}\n")


def ReadFile():    
    with open("testna1.txt") as dat:
        print(dat.read())

    
def main():
    AddToFile(7.3)
    AddToFile(14.7)
    AddToFile(32.1)

    ReadFile()


main()
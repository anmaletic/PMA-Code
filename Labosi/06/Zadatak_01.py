# Vježba 1:
# U ovoj vježbi je cilj vježbati osnovne operacije s listama.
# Napišite Python kôd koji će od korisnika tražiti unos cijelih brojeva koji predstavljaju 
# vrijednosti temperature u stupnjevima Celzijus. Neka je oznaka za kraj unosa vrijednost 99, 
# koja se ne uzima u obzir. Vrijednosti koje korisnik unosi se spremaju u listu 
# listaTemperatura. Nakon unosa je potrebno ispisati minimalnu i maksimalnu vrijednost 
# temperature u listi listaTemperatura na način da se koriste for ili while petlja za 
# pretragu minimalne i maksimalne vrijednosti.. Koja je složenost algoritma koji ste primijenili?


def GetMinMaxTemp(p_lista:list):
    _min:int
    _max:int
    for i in range(len(p_lista)):
        if i == 0:
            _min = p_lista[i]
            _max = p_lista[i]

        if p_lista[i] < _min:
            _min = p_lista[i]
        elif p_lista[i] > _max:
            _max = p_lista[i]

    return _min, _max


def GetMinMaxTempFE(p_lista:list):
    _min:int
    _max:int
    for num in p_lista:
        if p_lista.index(num) == 0:
            _min = num
            _max = num

        if num < _min:
            _min = num
        elif num > _max:
            _max = num

    return _min, _max

def main():
    listaTemp = []
    while True:
        unosTemp = int(input("Unesite temperaturu: "))
        
        if unosTemp != 99:
            listaTemp.append(unosTemp)
        else:
            break

    minTemp, maxTemp = GetMinMaxTemp(listaTemp)

    print(f"Min temp: {minTemp}")
    print(f"Max temp: {maxTemp}")

    minTemp, maxTemp = GetMinMaxTempFE(listaTemp)

    print(f"Min temp: {minTemp}")
    print(f"Max temp: {maxTemp}")


main()

# O(n)
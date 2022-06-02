



def RadixSort(lista:list):
    maxVrijednost = max(lista)
    maxExponent = len(str(maxVrijednost))
    sortiranaLista = lista[:]

    for exponent in range(maxExponent):
        pozicija = exponent + 1
        index = -pozicija

        digits = [[] for i in range(10)]

        for num in sortiranaLista:
            numAsAString = f"{num}"
            try:
                digit = numAsAString[index]
            except IndexError:
                digit = 0
            digit = int(digit)

            digits[digit].append(num)

        sortiranaLista = []
        for numeral in digits:
            sortiranaLista.extend(numeral)
    
    return sortiranaLista


def main():
    lista = []
    lista = [15, 56, 89, 45, 12, 65, 78, 45, 69, 12, 45, 2, 3, 74, 56, 44]

    # while  True:
    #     unos = int(input("Unesite broj: "))
    #     if unos == 11:
    #         break
    #     lista.append(unos)

    print(lista)

    result = RadixSort(lista)
    
    print(result)


main()
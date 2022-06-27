def vratiBrojac(text,ime):
    with open(text + '.txt', encoding='UTF-8') as file:
        dat = file.readlines()
        brojac = 0
        for imee in dat:
            if imee[:len(imee)-1] == ime:
                brojac += 1

        return brojac

print(vratiBrojac('popis','Andrija'))
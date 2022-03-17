# Vježba 1:
# Osobna iskaznica na poleđini ima MRZ (Machine Readable Zone) koji služi za elektronsko čitanje podataka sa
# osobne iskaznice. Napišite funkciju koja primi jedan takav string te ispišite podatke učitane iz MRZa. Podaci koje
# treba ispisati su:
# - Ime i prezime,
# - Datum, mjesec i godinu rođenja,
# - do kada vrijedi osobna,
# - državljanstvo osobe,
# - Spol osobe,
# - OIB


# Multi row


class MRZModel():
    def __init__(self):
        self.prezime = ""
        self.ime = ""
        self.datum = ""
        self.rok = ""
        self.drzava = ""
        self.spol = ""
        self.oib = ""

    def __str__(self) -> str:
        return (f"{self.ime} {self.prezime}\n{self.datum}\n{self.rok}\n{self.drzava}\n{self.spol}\n{self.oib}\n")


class MRZModelNoInit():
    prezime = ""
    ime = ""
    datum = ""
    rok = ""
    drzava = ""
    spol = ""
    oib = ""

    def __str__(self) -> str:
        return (f"{self.ime} {self.prezime}\n{self.datum}\n{self.rok}\n{self.drzava}\n{self.spol}\n{self.oib}\n")

        
def ReadMRZ(p_mrz):
    p_mrzObjekt = MRZModel()

    drugiRed = p_mrz.find("\n") + 1
    treciRed = p_mrz.find("\n", drugiRed) + 1

    p_mrzObjekt.prezime = p_mrz[treciRed : p_mrz.find("<", treciRed)]

    imeStartIndex = p_mrz.find("<", treciRed) + 2
    imeEndIndex = p_mrz.find("<", imeStartIndex)
    p_mrzObjekt.ime = p_mrz[imeStartIndex : imeEndIndex]

    p_mrzObjekt.datum = p_mrz[drugiRed : drugiRed + 6]
    p_mrzObjekt.spol = p_mrz[drugiRed + 7]
    p_mrzObjekt.rok = p_mrz[drugiRed + 8 : drugiRed + 14]
    p_mrzObjekt.drzava = p_mrz[drugiRed + 15 : p_mrz.find("<", drugiRed)]
    p_mrzObjekt.oib = p_mrz[15 : 26 ]

    return p_mrzObjekt


def main():

    mrz = "IOHRV987654321701234567890<<<<\n7701018M2006017HRV<<<<<<<<<<<7\nPREZIME<<IME<<<<<<<<<<<<<<<<<<"

    mrz_objekt = ReadMRZ(mrz)

    print(mrz_objekt)

main()
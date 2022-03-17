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


# Single row


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
        
def ReadMRZ(p_mrz):
    p_mrzObjekt = MRZModel()

    rowLength = int(len(p_mrz) / 3)

    prviRed = p_mrz[0:rowLength]
    drugiRed = p_mrz[rowLength:2*rowLength]    
    treciRed = p_mrz[2*rowLength:3*rowLength]

    print(prviRed)
    print(drugiRed)
    print(treciRed)

    p_mrzObjekt.prezime = treciRed[0 : treciRed.find("<")]

    imeStartIndex = treciRed.find("<") + 2
    imeEndIndex = treciRed.find("<", imeStartIndex)
    p_mrzObjekt.ime = treciRed[imeStartIndex : imeEndIndex]

    p_mrzObjekt.datum = drugiRed[0 : 6]
    p_mrzObjekt.spol = drugiRed[+ 7]
    p_mrzObjekt.rok = drugiRed[8 : 14]
    p_mrzObjekt.drzava = drugiRed[15 : drugiRed.find("<")]

    p_mrzObjekt.oib = prviRed[15 : 26 ]

    return p_mrzObjekt


def main():

    mrz = "IOHRV123456789701234567890<<<<7701018M2006017HRV<<<<<<<<<<<7PREZIME<<IME<<<<<<<<<<<<<<<<<<"

    mrz_objekt = ReadMRZ(mrz)

    print(mrz_objekt)

main()
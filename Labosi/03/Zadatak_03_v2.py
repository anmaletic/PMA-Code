# Vježba 3:
# Napisati program koja unutar rečenice pronalazi najduži palindrom. Ako su dvije (ili više) riječi
# palindromi iste dužine program ispisuje prvu od tih riječi.
# Palindromi su riječi koje se isto čitaju i s jedne i s druge strane (npr. kapak, oko).
# Za provjeru da li je riječ palindrom napisati funkciju.
# Primjeri rečenica i ispisa:
# - „Ovdje nema palindroma“ – program treba ispisati da nema palindroma
# - „Ana ide na posao“ – program treba ispisati „Ana“
# - „Ana vozi kajak“ – program ispisuje „kajak“
# - „Ana i Neven voze kajak“ - program ispisuje „Neven“.
# Voditi računa da se ne radi razlika između malih i velikih slova.


def RecenicaToRijec(p_recenica:str):
    rijeci = []
    startIndex = 0
    stopIndex = 0

    while stopIndex != -1:
        stopIndex = p_recenica.find(" ", startIndex)
 
        rijeci.append(p_recenica[startIndex : stopIndex if stopIndex != -1 else len(p_recenica)].lower())
        startIndex = stopIndex + 1

    return rijeci


def NadiPalindrom(p_rijeci:list):
    _palindrom = ("")    

    for rijec in p_rijeci:        
        _tempRijec = ""

        for i in range(len(rijec)):
            _tempRijec += rijec[-(i+1)]
        
        if (_tempRijec == rijec):
            if len(_tempRijec) > len(_palindrom):
                _palindrom = _tempRijec

    return _palindrom


def main():
    unosRecenica = ["Ovdje nema palindroma", "Ana ide na posao", "Ana vozi kajak", "Ana i Neven voze kajak"]

    for recenica in unosRecenica:            
        rijeci = RecenicaToRijec(recenica)
        palindrom = NadiPalindrom(rijeci)

        if(palindrom != ""):
            print(palindrom)
        else:
            print("Nema palindroma!")
            

main()
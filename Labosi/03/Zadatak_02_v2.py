# Vježba 2:
# Barbara Blackburn drži Guinnessov rekord u brzini tipkanja sa prosječnom brzinom od 150 riječi u minuti.
# Za natjecanje se pripremala tipkajući najpoznatiji pangram engleskog govornog područja (pangrami su
# rečenice u kojima se nalaze sva slova abecede):
# "The quick brown fox jumps over the lazy dog"
# No, tipkanje neprestano iste rečenice je zamorno i dosadno. Pomozite Barbari da dodatno ubrza svoje
# prste tako što ćete joj izraditi program za pronalazak pangrama: program neka korisnika upita jednu
# rečenicu, te ispiše je li ona pangram ili nije.


def isPangramASCII(recenica:str):
    skup = set()

    for slovo in recenica:
        asciiKod = ord(slovo.upper())
        if asciiKod >= 65 and asciiKod <= 90:
            skup.add(chr(asciiKod))

    return len(skup) == 26


def isPangramAlpha(recenica:str):
    skup = set()

    for slovo in recenica:
        slovoUP = slovo.upper()
        if slovoUP.isalpha():
            skup.add(slovoUP)

    return len(skup) == 26




def main():
    #   unosRecenica = input("Unesite recenicu: ")
    unosRecenica = "The quick brown fox jumps over the lazy dog 123"
    print(isPangramASCII(unosRecenica))
    print(isPangramAlpha(unosRecenica))

main()
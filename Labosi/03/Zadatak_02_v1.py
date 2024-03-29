# Vježba 2:
# Barbara Blackburn drži Guinnessov rekord u brzini tipkanja sa prosječnom brzinom od 150 riječi u minuti.
# Za natjecanje se pripremala tipkajući najpoznatiji pangram engleskog govornog područja (pangrami su
# rečenice u kojima se nalaze sva slova abecede):
# "The quick brown fox jumps over the lazy dog"
# No, tipkanje neprestano iste rečenice je zamorno i dosadno. Pomozite Barbari da dodatno ubrza svoje
# prste tako što ćete joj izraditi program za pronalazak pangrama: program neka korisnika upita jednu
# rečenicu, te ispiše je li ona pangram ili nije.


def Pangram_1(recenica:str):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for slovo in recenica.lower():
        if slovo != " " and slovo in abc:
            abc = abc.replace(slovo, "")

    if abc == "":
        print("Recenica je pangram!")
    else:
        print("Recenica nije pangram!")


def Pangram_2(recenica:str):
    abc = "abcdefghijklmnopqrstuvwxyz"
    for slovo in recenica.lower():
        if slovo != " " and abc.find(slovo) != -1:
          abc = abc.replace(slovo, "")

    if abc == "":
        print("Recenica je pangram!")
    else:
        print("Recenica nije pangram!")




def main():
    #   unosRecenica = input("Unesite recenicu: ")
    unosRecenica = "The quick brown fox jumps over the lazy dog"
    Pangram_1(unosRecenica)
    Pangram_2(unosRecenica)


main()
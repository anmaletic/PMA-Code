# Špil se sastoji iz 52 igrače karte. Svaka od njih može biti jedna od četiri boje te jedna od 13
# vrijednosti. Boje su: pik, herc, karo i tref. Vrijednosti su: 2,3,4,5,6,7,8,9,10, as, dečko, dama i
# kralj. Definirajte klasu Karta, koja sadrži konstruktor koji postavlja vrijednosti atributa boja te
# atributa vrijednost. Imate slobodu odabira načina mapiranja boja te vrijednosti većih od 9.
# Klasa ima i metodu __str__ koja ispisuje podatke o jednoj karti – boju i vrijednost. Definirajte
# klasu Spil koji se programski popunjava vrijednostima klase Karta. Ispišite špil karata. Unutar
# klase Spil definirajte metode uzmiKartu te dodajKartu koja pri pozivu uzimaju kartu iz špila
# te dodaju kartu u špil.
# Testirajte obje klase na način da
# - ispišete špil karata nakon kreiranja
# - ispišete kartu koja je uzeta iz špila te špil nakon uzimanja karte/karata


class Karta():
    def __init__(self, p_boja, p_vrijednost):
        self.boja = p_boja
        self.vrijednost = p_vrijednost

    def __str__(self):
        return f"{self.boja} {self.vrijednost}"

    
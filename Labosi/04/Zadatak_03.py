# Potrebno je:
# - proširiti klasu Covjek iz Vježbi 1 i 2 na način da joj se dodaju još dvije statičke 
# varijable _brM i _brZ koje su cjelobrojne vrijednosti koje označavaju broj muških, 
# odnosno ženskih osoba. Potrebno ih je inicijalizirati na vrijednost 0.
# - Kreirati statičku metodu uvecajSpol koja ima ulazni parametar spol koja je string 
# vrijednost. Metoda za 1 uveća statičku varijablu za odgovarajući spol koji je predan 
# kao parametar. 
# Npr., ako je kao vrijednost predana vrijednost 'M' tada se za 1 uveća vrijednost 
# varijable _brM. Ako je kao vrijednost predana vrijednost 'Z' tada se za 1 uveća 
# vrijednost varijable _brZ. 
# U svakom slučaju je potrebno ispisati odgovarajuću poruku kada su predane 
# vrijednosti 'M' i 'Z' a kroz izuzetak hvatati predavanje neke druge vrijednosti za 
# parametar spol.
# - Ispisati konačno stanje varijabli _id, _brM i _brZ te potvrdite da vrijedi _id = 
# _brM+_brZ

class NeispravanUnos(Exception):
    pass

class Covjek(object):
    _id = 0
    _brZ = 0
    _brM = 0
    _imeiprezime = "Pero Perić"

    def __init__(self) -> None:
        Covjek._id += 1
    
    @staticmethod
    def UvecajSpol(_spol:str):
        try:
            _spol = _spol.upper()
            if _spol == "M":
                Covjek._brM += 1
                print("Broj muških osoba uvecan za 1.")    
            elif _spol == "Z":
                Covjek._brZ += 1
                print("Broj ženskih osoba uvecan za 1.")
            else:
                raise NeispravanUnos(f"Unos mora biti M ili Z! (Unos: {_spol})")
        except NeispravanUnos as e:
            print(e)     

    
def main():
    Covjek.UvecajSpol("m")
    Covjek.UvecajSpol("ž")
    Covjek.UvecajSpol("Z")
    Covjek.UvecajSpol("Z")
    Covjek.UvecajSpol("M")    

    osoba1 = Covjek()
    osoba1.UvecajSpol("M")



    print(f"Broj muških: {Covjek._brM}")
    print(f"Broj ženskih: {Covjek._brZ}")


main()
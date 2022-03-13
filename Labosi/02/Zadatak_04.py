# Vježba 4:
# Ova vježba ima za svrhu ponavljanje rada s globalnim i lokalnim varijablama.

# Kreirajte Python program koji će definirati globalnu varijablu _globalVar i inicijalizirajte joj
# vrijednost na 'noć'.
# Ako definiramo dijelove dana na sljedeći način:
# [06:00 – 10:00> : 'jutro'
# [10:00 – 12:00> : 'prijepodne'
# [12:00 – 17:00> : 'poslijepodne'
# [17:00 – 22:00> : 'večer'
# [22:00 – 06:00> : 'noć'
# kreirajte unutar Python programa nakon globalne varijable _globalVar funkciju getDioDana
# koja će dohvatiti sistemsko vrijeme te generirati slučajan broj u rasponu od 0 do 12 te
# dobiveni broj dodati na broj sati sistemskog vremena. Prema navedenoj tablici o dijelovima
# dana, ako je dobiveni raspon drukčiji od inicijalnog 'noć' promijeniti vrijednost globalne
# varijable.
# Ispišite inicijalnu vrijednost globalne varijable, dobiveno sistemsko vrijeme, izmijenjeno
# sistemsko vrijeme te završnu vrijednost globalne varijable.

from datetime import datetime
from random import randint

_globalVar = "noć"

class DanModel():
    def __init__(self, p_naziv, p_pocetak, p_kraj):
        self.naziv = p_naziv
        self.pocetak = p_pocetak
        self.kraj = p_kraj


def FillDanData(p_DanData:list):
    p_DanData.append(DanModel("jutro", 6, 10))
    p_DanData.append(DanModel("prijepodne", 10, 12))
    p_DanData.append(DanModel("poslijepodne", 12, 17))
    p_DanData.append(DanModel("večer", 17, 22))
    p_DanData.append(DanModel("noć", 22, 6))

   
def GetDioDana(p_DanData:list):
    global _globalVar
    vrijeme = datetime.now()
    offset = randint(0, 12)        
    print(f"Sistemsko vrijeme: {vrijeme.strftime('%H:%M')}")

    sat = vrijeme.hour + offset

    vrijeme = vrijeme.replace(hour= sat if sat < 24 else sat - 24)
    print(f"Izmjenjeno vrijeme: {vrijeme.strftime('%H:%M')}")

    for dio in p_DanData:
        dio:DanModel
        if vrijeme.hour >= dio.pocetak and vrijeme.hour < dio.kraj:
            _globalVar = dio.naziv
            break


def main():       
    DanData = []
    FillDanData(DanData)
    print(f"Globalna varijabla: {_globalVar}")

    GetDioDana(DanData)
    print(f"Globalna varijabla: {_globalVar}")


main()


# Vježba 2:
# Kreirati funkciju zaokruzenoVrijeme koja će sistemsko vrijeme zaokružiti na prvih sljedećih
# 15 minuta. Zbog pojednostavljenja kôda, zanemarimo mogućnost da ćete dobiti sistemsko
# vrijeme koje je točno 21:15:00 i slične vrijednosti.

from datetime import datetime, timedelta

def ispisVremenaKorak15():
    vrijeme = datetime.now()
    
    if vrijeme.minute > 45:
        minute = 0
        hour = vrijeme.hour + 1
        print(f"{hour}:{minute}")
        return
    elif vrijeme.minute > 30:
        minute = 45
    elif vrijeme.minute > 15:
        minute = 30
    else:
        minute = 15

    print(f"{vrijeme.strftime('%H')}:{minute}")

def ispisVremenaKorak15Object():
    vrijeme = datetime.now()
    
    if vrijeme.minute > 45:
        vrijeme = vrijeme.replace(hour = vrijeme.hour + 1, minute = 0)
    elif vrijeme.minute > 30:
        vrijeme = vrijeme.replace(minute = 45)
    elif vrijeme.minute > 15:
        vrijeme = vrijeme.replace(minute = 30)
    else:
        vrijeme = vrijeme.replace(minute = 15)

    print(vrijeme.strftime('%H:%M'))

def ispisVremenaKorak60():
    vrijeme = datetime.now()

    if vrijeme.minute > 15:
        print(f"{vrijeme.hour + 1}:15")
    else:
        print(f"{vrijeme.hour}:15")

def ispisVremenaKorak60Object():
    vrijeme = datetime.now()

    if vrijeme.minute > 15:
        vrijeme = vrijeme.replace(hour = vrijeme.hour + 1, minute = 15)
        print(vrijeme.strftime('%H:%M'))
    else:
        vrijeme = vrijeme.replace(minute = 15)
        print(vrijeme.strftime('%H:%M'))
        vrijeme.replace()

def ispisVremena():
    vrijeme = datetime.now()
    razlika = (datetime.min - datetime.now()) % timedelta(minutes=15)
    zaokr = vrijeme + razlika
    print(zaokr)

def main():
    ispisVremenaKorak15()
    ispisVremenaKorak60()
    ispisVremenaKorak60Object()
    ispisVremenaKorak15Object()
    ispisVremena()

    minTest = datetime.now().minute
    print(minTest)


main()
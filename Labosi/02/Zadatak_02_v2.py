from datetime import datetime
import random


def getDioDana():
    h = datetime.now().hour
    x = random.randint(0,12)

    _globalVar:str
    incH = h + x
    if incH >= 6 and incH < 22:
        _globalVar = "jutro"

    print(_globalVar)

getDioDana()
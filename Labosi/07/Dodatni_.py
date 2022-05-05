# metoda Count rekurzivno



def BrojimZnakove(tekst:str, znak:str):
    if len(tekst) == 0:
        return 0
    return (1 + BrojimZnakove(tekst[1:], znak)) if tekst.startswith(znak) else (0 + BrojimZnakove(tekst[1:], znak))


print(BrojimZnakove("aaa", "aa"))
    
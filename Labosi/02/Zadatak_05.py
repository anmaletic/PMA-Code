# Vježba 5:
# Napišite program koji prima broj sekundi, a vraća koliko je to sati, minuta, sekundi.
# Npr. ako je unešeni broj 45896, program treba ispisati 12sati,44minute i 56sekundi


def ConvertSecToTime(p_sec):
    p_sati = p_sec // 3600
    p_minute = (p_sec % 3600) // 60
    p_sekunde = (p_sec % 3600) % 60

    return p_sati, p_minute, p_sekunde


def main():
    unosSec = int(input("Unesite vrijeme u sekundama: "))

    sati, minute, sekunde = ConvertSecToTime(unosSec)

    print(f"{unosSec} = {sati}h {minute}m {sekunde}sec")


main()
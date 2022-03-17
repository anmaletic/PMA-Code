# 6.
# Deklarirati svoj izuzetak mojaProvjera. Implementirati ga u Python kodu koji provjerava ako
# smo dva puta zaredom generirali slučajni broj koji je manji od 10 te u slučaju da se dva puta zaredom
# generira slučajni broj manji od 10 raise-ati svoj izuzetak s odgovarajućom porukom.


import random


class mojaProvjera(Exception):
    pass


def main():
    counter = 0
    while True:
        try:
            num = random.randint(7,1000)
            if(num < 10):
                counter += 1                
            else:
                counter = 0

            if(counter == 2):
                raise mojaProvjera(f"Dva puta generiran isti broj: {num}")

        except mojaProvjera as e:
            print(e)

    
main()
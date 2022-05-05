# Vježba 3:
# U ovoj vježbi je cilj vježbati rad s tekstualnim datotekama.
# Potrebno je napisati Python kod koji će čitati sadržaj tekstualne datoteke testna.txt liniju 
# po liniju te iz svake linije ispisati zadnji znak.


def PrintLastChar():
    with open("testna.txt") as dat:
        for line in dat:
            print(line.replace("\n", "")[-1])


def main():
    PrintLastChar()


main()
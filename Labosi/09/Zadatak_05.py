# Vježba 5:
# U ovoj vježbi je cilj vježbati rad s direktorijima.
# Datoteke su organizirane u mape (direktorije). Inicijalno, kod pokretanja Python programa, 
# 'gleda' se trenutni direktorij. Vaš je zadatak istražiti modul os i mogućnosti rada s datotekama 
# i direktorijima.
# Potrebno je napraviti program koji će demonstrirati:
# - kako se ispisuje apsolutna staza do datoteke, 
# - kako se provjerava postojanje datoteke te 
# - kako se provjerava je li predani parametar direktorij. 
# Na kraju je potrebno napisati program koji ispisuje nazive svih datoteka u trenutnom 
# direktoriju te njegovim poddirektorijima.

import os


dirPath = "C:\\Users\\Korisnik\\OneDrive\\Vsite\\2. godina\\4. semestar\\PMA\\PMA-Code\\Labosi\\09"
fileName = "Zadatak_05.py"
filePath = os.path.join(dirPath, fileName)

print(filePath)
print()

absPath = os.path.abspath(fileName)
print(f"Absolut path = {absPath}")

fileExists = os.path.exists(filePath)
print(f"FileExists = {fileExists}")

isDir = os.path.isdir(filePath)
print(f"IsDir = {isDir}")

print(os.path.curdir)

files = os.listdir(dirPath)
print(files)

def printAllFiles(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path,file)):
            print(file)
        elif os.path.isdir(os.path.join(path,file)):
            printAllFiles(os.path.join(path,file))

printAllFiles(os.path.dirname(os.path.realpath(__file__)))


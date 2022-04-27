matrica = []
a = 3
b = 3
for i in range(a):
    podA = []
    for i in range(b):
        podA.append(int(input('Unesite cijeli broj: ')))
    matrica.append(podA)
for redak in matrica:
    print(redak)
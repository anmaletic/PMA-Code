

l = [2, 5, 4, 7, 8, 0, 2, 0]

min = min2 = min3 = max(l)

for i in range(len(l)):
    if l[i] < min:
        min3 = min2
        min2 = min
        min = l[i]
    elif l[i] < min2:
        min3 = min2
        min2 = l[i]
    elif l[i] < min3:
        min3 = l[i]

print(min, min2, min3)
print(min + min2 + min3)

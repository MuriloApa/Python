x, y, z = map(int, input().split())

vet = []
vet.append(x)
vet.append(y)
vet.append(z)

for i in range(1, len(vet)):
    aux = vet[i]
    j = i
    while j > 0 and aux < vet[j - 1]:
        vet[j] = vet[j-1]
        j -= 1
    vet[j] = aux


for i in vet:
    print(i)

print("")
print(x, y, z, sep = "\n")

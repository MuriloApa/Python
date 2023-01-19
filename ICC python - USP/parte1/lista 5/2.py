x=int(input("digite a largura: "))
y=int(input("digite a altura: "))
for i in range(0, y):
    for j in range (0, x):
        if i==0 or i==y-1:
            print("#", end="")
        else:
            if j!=0 and j!=x-1:
                print(" ", end="")
            else:
                print("#", end="")
    print()
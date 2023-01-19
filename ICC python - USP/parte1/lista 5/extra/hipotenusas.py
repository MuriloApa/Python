def é_hipotenusa(x):
    for i in range(1, x+1):
        for j in range(1, x+1):
            if i**2+j**2==x**2:
                return True

def soma_hipotenusas(n):
    cont=0
    for i in range(1, n+1):
        if é_hipotenusa(i):
            cont=cont+i
    return cont


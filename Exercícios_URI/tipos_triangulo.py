a, b, c = map(float, input().split())

if (b > a):
    aux = b
    b = a
    a = aux
if (c > a):
    aux = c
    c = a
    a = aux


if (a >= (b+c)):
    print("NAO FORMA TRIANGULO")
else:
    if (a**2 == (b**2 + c**2)):
        print("TRIANGULO RETANGULO")
    else:
        if (a**2 >(b**2 + c**2)):
            print("TRIANGULO OBTUSANGULO")
        else:
            print("TRIANGULO ACUTANGULO")
if (a == b and b == c):
    print("TRIANGULO EQUILATERO")
else:
    if (a == b or a == c or b == c):
        print("TRIANGULO ISOSCELES")

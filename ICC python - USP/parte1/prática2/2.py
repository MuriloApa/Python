def main():
    import math
    a=float(input("Entre com o coeficiente a\n"))
    b=float(input("Entre com o coeficiente b\n"))
    c=float(input("Entre com o coeficiente c\n"))
    delta=b**2-4*a*c
    if delta<0:
        print("esta equação não possui raízes reais")
    else:
        if delta==0:
            print("a raiz dupla desta equação é", -b/(2*a))
        else:
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
            if x1<x2:
                print("as raízes da equação são", x1, "e", x2)
            else:
                print("as raízes da equação são", x2, "e", x1)
main()
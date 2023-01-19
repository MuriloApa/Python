def main():
    import math
    x1=int(input("Entre com a coordenada x do primeiro ponto\n"))
    y1=int(input("Entre com a coordenada y do primeiro ponto\n"))
    x2=int(input("Entre com a coordenada x do segundo ponto\n"))
    y2=int(input("Entre com a coordenada y do segundo ponto\n"))
    d=math.sqrt((x1-x2)**2+(y1-y2)**2)
    if d<10:
        print("perto")
    else:
        print("longe")
main()
def busca(lista, x):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim)//2
        print(meio)
        if lista[meio] == x:
            return meio
        else:
            if x > lista[meio]:
                inicio = meio + 1
            else:
                fim = meio -1
    return False

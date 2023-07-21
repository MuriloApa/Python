def bubble_sort(lista_origin):
    lista = lista_origin[:]
    for i in range(len(lista) - 1, 0, -1):
        for j in range(0, i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(lista)
    return lista
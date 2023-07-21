def insertion_sort(lista_origin):
    lista = lista_origin[:]
    for i in range(1, len(lista)):
        menor = lista[i]
        j = i
        while j > 0 and menor < lista[j-1]:
            lista[j] = lista[j-1]
            j -= 1
        lista[j] = menor
    return lista
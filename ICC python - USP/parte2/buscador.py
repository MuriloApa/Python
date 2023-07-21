class buscador:

    def sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1
    
    def binaria(self, lista, x):
        inicio = 0
        fim = len(lista) - 1
        while inicio <= fim:
            meio = (fim+inicio)//2
            if lista[meio] == x:
                return meio
            else:
                if lista[meio] < x:
                    inicio = meio + 1
                    print("Início =", inicio, ", fim =", fim)
                else:
                    fim = meio - 1
                    print("Início =", inicio, ", fim =", fim)
        return -1
    
busc = buscador()
print(busc.binaria([1, 6, 7, 8, 9, 15, 17, 18, 30, 45], 1))
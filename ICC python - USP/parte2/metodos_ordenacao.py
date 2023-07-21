import random

class Metodos_ordenacao:

    def lista_aleatoria(self, n):
        return [random.randrange(1000) for x in range(n)]
    
    def lista_ordenada(self, n):
        return [x for x in range(n)]
    
    def lista_quase_ordenada(self, n):
        lista = self.lista_ordenada()
        lista[n//10] = -500
        return lista

    def selecao_direta(self, lista):
        for i in range(len(lista)-1):
            menor = i
            for j in range(i+1, len(lista)):
                if lista[j] < lista[menor]:
                    menor = j
            lista[i], lista[menor] = lista[menor], lista[i]

    def bubblesort(self, lista):
        for i in range(len(lista)-1, 0, -1):
            for j in range(0, i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]

    """ def bubblesort_melhorado(lista):
        troca = True
        i = len(lista)-1
        while i >= 0 and troca == True:
            j = 0
            troca = False
            while j < i:
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    troca = True
                j += 1
            i -= 1 """
        
    def bubblesort_melhorado(self, lista):
        for i in range(len(lista)-1, 0, -1):
            troca = False
            for j in range(0, i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]    
                    troca = True
            if not troca:
                return        

    def insertionSort(self, lista):
        for i in range(1, len(lista)):
            menor =  lista[i]
            j = i
            while(j > 0 and menor < lista[j-1]):
                lista[j] = lista[j-1]
                j -= 1
            lista[j] = menor

if __name__ == "__main__":
    from time import time

    continua = True

    while(continua):
        n = int(input("Digite o tamanho do vetor: "))

        ordenador = Metodos_ordenacao()
        lista = ordenador.lista_aleatoria(n)

        aux = lista[:]
        aux2 = lista[:]
        aux3 = lista[:]
        ordenador = Metodos_ordenacao()
        antes = time()    
        ordenador.insertionSort(lista)
        depois = time()
        print(f"InsertionSort = {(depois-antes):.2f}s")
        antes = time()    
        ordenador.bubblesort(aux)
        depois = time()
        print(f"bubblesort = {(depois-antes):.2f}s")
        antes = time()    
        ordenador.selecao_direta(aux2)
        depois = time()
        print(f"selecao_direta = {(depois-antes):.2f}s")
        antes = time()    
        ordenador.bubblesort_melhorado(aux3)
        depois = time()
        print(f"bubblesort melhorado = {(depois-antes):.2f}s")

        continua = (input("Deseja continuar? S ou N: "))
        if continua == "S" or continua == "s":
            continua = True
        else:
            continua = False
    
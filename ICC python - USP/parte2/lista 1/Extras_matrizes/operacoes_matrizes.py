def main():
    lista_elementos_decrescente()

def le_matriz():
    m = int(input("Digite o número de linhas: "))
    n = int(input("Digite o número de colunas: "))
    matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            print("Digite o elemento (", i, " ,", j, "): ", sep="", end="")
            valor = int(input())
            linha.append(valor)
        matriz.append(linha)

    return matriz

def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == len(matriz[i]) - 1:
                print(matriz[i][j])
            else:
                print(matriz[i][j], end=" ")

def simetrica(matriz):
    """
        (matriz) → bool

        return true if the matriz recivied is simetric or false case not
    """
    ver = True
    i = 0
    while (i < len(matriz) and ver):
        j = 0
        while (j < i):
            if matriz[i][j] != matriz[j][i]:
                ver = False
            j+=1
        i+=1

    return ver

def le_ver_simetrica():
    m = le_matriz()
    if simetrica(m):
        imprime_matriz(m)
    else:
        print("Não é uma matriz simétrica.")

def zeradas(m):
    linhas = [[True] * len(m)]
    
    colunas = [[True] * len(m[0])]
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != 0:
                linhas[0][i] = False
                colunas[0][j] = False
    
    cont_linhas = 0
    cont_colunas = 0
    print(linhas)
    print(colunas)
    for i in range(len(linhas[0])):
        if linhas[0][i]:
            cont_linhas += 1

    for i in range(len(colunas[0])):
        if colunas[0][i]:
            cont_colunas += 1

    print("Linhas zeradas:", cont_linhas, "\nColunas zeradas:", cont_colunas)

def le_Conta_zeradas():
    matriz = le_matriz()
    zeradas(matriz)

def multiplica_matriz(m1, m2):
    """
        This function returns the  multiplication between m1 and m2
    """
    result = False
    if len(m1[0]) == len(m2):
        result = []
        for i in range(len(m1)):
            linha = []
            for j in range(len(m2[0])):
                soma = 0
                for k in range(len(m2)):
                    soma += m1[i][k] * m2[k][j]
                linha.append(soma)
            result.append(linha)
    return result

def le_multiplica():
    print("Para a primeira matriz")
    A = le_matriz()
    print("Para a segunda matriz")
    B = le_matriz()
    C = multiplica_matriz_2(A, B)
    if C != False:
        print("Resultado:")
        imprime_matriz(C)
    else:
        print("A multiplicação não é possível de ser realizada")

def produto_lincol(lin, a_mat, col, b_mat):
    """
        Devolve o produto escalar entre a lin de a e col de b
    """
    soma = 0
    for i in range(len(a_mat[lin])):
        soma += a_mat[lin][i] * b_mat[i][col]
    return soma

def multiplica_matriz_2(m1, m2):
    result = []
    for i in range(len(m1)):
        linha = []
        for j in range(len(m2[0])):
            soma = produto_lincol(i, m1, j, m2)
            linha.append(soma)
        result.append(linha)
    return result

def acha_max(A, dif = None):
    '''(matriz) -> int, int, int

    Recebe uma matriz A e devolve 3 inteiros:
    k (um maior valor), e sua posicao lin, col.
    '''
    maior = A[0][0]
    lin = 0
    col = 0
    if dif == None:
        for i in range (len(A)):
            for j in range(len(A[i])):
                if A[i][j] > maior:
                    maior = A[i][j] 
                    lin = i
                    col = j
        return [maior, lin, col]
    else:
        for i in range (len(A)):
            for j in range(len(A[i])):
                if A[i][j] >= maior and A[i][j] < dif:
                    maior = A[i][j] 
                    lin = i
                    col = j
        return [maior, lin, col]

def lista_elementos_decrescente():
    M = le_matriz()
    interacao = acha_max(M)
    print("Elem\tLinha\tColuna\n")
    for i in range(len(M) * len(M[0])):
        print(interacao[0], interacao[1], interacao[2], sep="\t")
        interacao = acha_max(M, interacao[0])
main()
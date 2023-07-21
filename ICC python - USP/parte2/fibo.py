def fib(n):
    """
        imprime os n primeiros termos da sequência de fibonacci
    """
    a, b = 0, 1
    cont = 0
    while(cont < n):
        print(b, end=" ")
        a, b = b, a + b
        cont += 1

def fib2(n):
    """
        This function returns the fibonacci's list for the first n numbers
    """
    a, b = 0, 1
    cont = 0
    list = []
    while(cont < n):
        list.append(b)
        a, b = b, a + b
        cont += 1
    return list

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

"""
    → A variável __name__ permite que um arquivo python possa ser tanto usado como script quanto como um módulo a ser importado.
    → O exemplo utilizado acima está disponível na documento online da linguagem Python para a versão 3.11.1 (visto em 18 de janeiro de 2023).
"""
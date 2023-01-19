x=int(input("Entre com um número positivo: "))
while (x>0):
    
    # Explicação: Já se começa dividindo pelo 2 e o laço ira repetir enquanto a divisão de x pela variável div
    # repare que o while n chega até  a divisão de x por ele mesmo, pois a partir de x/2 a divisão sempre sera um 
    # número quebrado, então quando acabar o laço, ou chegou-se a metade do numero ou achou-se um divisor antes do 
    # esperado. Ao sair, se a divisão de x por div for exata, achamos um divisor que não é o próprio x, então ele não é primo
    if x!=2:
        div=2
        while (x%div!=0 and div<=x/2):
            div=div+1
        if x%div==0:
            print(x, "não é primo.")
        else:
            print(x, "é primo.")
    else:
        print(x, "é primo.")
    x=int(input("Entre com o próximo número: "))

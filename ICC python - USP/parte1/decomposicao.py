def main():
    x=int(input("Entre com um número inteiro: "))
    x2=x
    primo=2
    fatores=[]
    while x>1:
        indice=0
        while x%primo==0:
            x=x//primo
            fatores.append(primo)
            indice=indice+1
        if indice!=0:
            print("Multiplicidade do", primo, "= ", indice)
        if x!=1:
            primo=novo_primo(primo)
    print(x2, "= ", end=" ")
    for j in range(len(fatores)):
        if j!=(len(fatores)-1):
            print(fatores[j], "*", end=" ")
        else:
            print(fatores[j])

def novo_primo(x):
    new_primo=x
    i=x+1
    while new_primo==x:
        div=0
        for j in range(1, i+1):
            if i%j==0:
                div=div+1
        if div==2:
            new_primo=i
        i=i+1
    return new_primo

main()
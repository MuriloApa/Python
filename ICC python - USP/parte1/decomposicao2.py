def main():
    x=int(input("Entre com um número inteiro: "))
    x2=x
    primo=2
    fatores=[]
    indice=-1
    if x==1:
        print(f"1 = 1\nMultiplicidade do 1 = 1")
    else:
        while x>1:
            if x%primo==0:
                x=x//primo
                fatores.append(primo)
                indice=indice+1
            else:
                if x!=1:
                    primo=novo_primo(primo)
        print(x2, "= ", end=" ")
        for j in range(len(fatores)):
            if j!=(len(fatores)-1):
                print(fatores[j], "*", end=" ")
            else:
                print(fatores[j])
        for i in range(0, fatores[indice]+1):
            q=0
            for j in range(len(fatores)):
                if i==fatores[j]:
                    q=q+1
            if q!=0:
                print("Multiplicidade do", i, "= ", q)
                
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
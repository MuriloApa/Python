n=int(input("Digite um número inteiro: "))
div=0
for i in range(1,n):
    if n%i==0:
        div+=1
if div==1:
    print("primo")
else:
    print("não primo")
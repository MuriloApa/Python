n1=int(input("Digite um número inteiro: "))
s=0
while n1>0:
    s=s+n1%10
    n1=n1//10
print(s)
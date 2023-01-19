n=int(input("Digite um número inteiro: "))
anterior=n%10
atual=n//10%10
while anterior!=atual and n!=0:
    n=n//10
    anterior=n%10
    atual=n//10%10
if n==0:
    print("não")
else:
    print("sim")
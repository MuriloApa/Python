x=int(input("Entre com o primeiro número, as leituras pararão ao digitar 0: "))
vet=[]
while x!=0:
	vet.append(x)
	x=int(input("Entre com o próximo"))
for i in range((len(vet)-1),-1,-1)):
	print(vet[i])
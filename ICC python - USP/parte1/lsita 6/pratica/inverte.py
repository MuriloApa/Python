a=[]
n=int(input("Digite um número: "))
while n!=0:
	a.append(n)
	n=int(input("Digite um número: "))
for i in range(-1, -1*((len(a))+1), -1):
	print(a[i])

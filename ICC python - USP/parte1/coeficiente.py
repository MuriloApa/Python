def main():
	n=int(input("Entre com n "))
	k=int(input("Entre vom o k "))
	print("O coeficiente binomial para dos números dados é", coef_binomial(n, k))
	
def fatorial (x):
	pot=1
	for i in range(1, x+1):
		pot=pot*i
	return pot
def coef_binomial (n, k):
	c=fatorial(n)//(fatorial(k)*fatorial(n-k))
	return c     

main()

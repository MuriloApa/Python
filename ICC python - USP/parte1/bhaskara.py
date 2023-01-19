import math
def delta (a, b, c):
	return b**2-4*a*c
def bhaskara (a, b, c):
	Delta=delta(a, b,c)
	if Delta<0:
		print("Não há raízes reais")
	else:
		if Delta==0:
			print("A equação possui apenas uma raíz, x =", -b/(2*a))
		else:
			print("A equação possui duas raízes reais distintas, x1 =", (-b+math.sqrt(Delta))/(2*a), "e x2 =", (-b-math.sqrt(Delta))/(2*a))
def main():
	a=int(input("Entre com o coeficiente a "))
	b=int(input("Entre com o coeficiente b "))
	c=int(input("Entre com o coeficiente c "))
	bhaskara(a, b,c)
main()

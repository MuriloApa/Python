import fibo as f

fibonacci = f.fib2

print(fibonacci(15))

print(__name__)
print(f.__name__)

#A maneira de importar abaixo coloca todas as funções do módulo math no escopo do programa principal

from math import * 

#A função "comb" retorna as 2-combinações para um conjunto de 10 elementos
print(comb(10,2))
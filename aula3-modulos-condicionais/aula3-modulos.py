import math # importa biblioteca math

num = 17

raiz = math.sqrt(num) # utiliza função sqrt() (raiz) da biblioteca math para calcular
print(f"A raiz de {num} é {raiz:.2f}") # printa os resultados | :.2f limita 2 casas decimais

graus = 60
radiano = graus / 180 / math.pi
seno = math.sin(radiano)
print(seno)



import random # importa biblioteca random

num_random = random.random()
print(num_random*10)

num_rand_int = random.randint(1,10)
print(num_rand_int)


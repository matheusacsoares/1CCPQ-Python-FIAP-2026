# ▪ Faça um programa que leia 2 valores inteiros (A e B).
# ▪ A seguir, o programa deve mostrar uma mensagem "São Múltiplos" ou "Não são Múltiplos", indicando se os valores lidos são múltiplos entre si.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 % n2 == 0:
    print(f"{n1} é múltiplo de {n2}")
elif n2 % n1 == 0:
    print(f"{n2} é multiplo de {n1}")
else:
    print("Os números não são múltiplos!")
# Faça um programa que leia um número, e informe se ele é par ou impar

n = int(input("Digite um número: "))

if n % 2 == 0:
    print(f"{n} é um número par")
else:
    print(f"{n} é um número impar")
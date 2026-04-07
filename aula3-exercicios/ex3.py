# Faça um programa que peça dois números e imprima o maior deles, e informe caso eles sejam iguais

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 == n2:
    print("Os números são iguais!")
elif n1 > n2:
    print(f"{n1} é o maior número digitado!")
elif n2 > n1:
    print(f"{n2} é o maior número digitado!")
# Escreva um algoritmo que recebe dois números e um caractere (representando uma das operações matemáticas (+, -, *, /)
# O programa deve calcular o valor final de acordo com a operação selecionada.
from sympy import false

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
operador = input("Digite a operação desejada (+, -, *, /) : ")
erro = False

if operador == '+':
    operacao = 'soma'
    resultado = n1 + n2
elif operador == '-':
    operacao = 'subtração'
    resultado = n1 - n2
elif operador == '*':
    operacao = 'multilicação'
    resultado = n1 * n2
elif operador == '/':
    operacao = 'divisão'
    resultado = n1 / n2
else:
    erro = True
    print("ERRO: Operação não é valida!")

if erro != True:
    print(f"O resultado da {operacao} de {n1} e {n2} é {resultado}")


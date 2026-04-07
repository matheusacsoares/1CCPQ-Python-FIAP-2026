# Faça um programa para a leitura de quatro notas parciais de um aluno. O programa deve calcular a média alcançada pelo aluno e apresentar

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print("Aprovado!")
elif media >= 5 and media < 7:
    print("Em recuperação")
elif media < 5:
    print("Reprovado!")

'''
Desafio 2: Cálculo de Média e Status do Estudante
Dadas as 4 notas de um estudante, calcule sua média e, com base nela, emita a mensagem
de status correspondente:
1. Aprovado: Média estritamente maior que 7.
2. Recuperação: Média entre 5 (inclusive) e 7 (inclusive).
3. Reprovação: Média estritamente abaixo de 5.
'''

notas  = []

total = 0

for i in range(4):

    i +=1

    n = float(input(f"Informa a nota  do {i}° Bimestre:\n"))

    notas.append(n)

for i in range(4):

    total += notas[i]

if total/4 >7:

    print(f"Aprovado: {total/4}")

elif total/4 <= 7:

    print(f"Recuperação: {total/4}")

elif total/4 <= 5:

    print(f"Reprovado: {total/4}")
'''
Desafio 1: Ordenação de Três Números
Recebidos 3 números inteiros, crie um programa que os mostre ordenados em ordem
crescente
'''
number = []

for i in range(3):
    i += 1

    n = int(input(f"Informe o {i}° inteiro: "))

    number.append(n)

max = max(number)

min = min(number)

for i in range(3):

    if max > number[i] > min:
        print(min, number[i], max)

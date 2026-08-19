'''
5. Média do Aluno com Optativa:
Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação
optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve
ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa
substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e
mensagens que indiquem se o estudante foi aprovado, reprovado ou se está em
recuperação, de acordo com as informações abaixo:
Aprovado: média >= 6.0
Reprovado: média < 3.0
Recuperação: média >= 3.0 e < 6.0

Observação: nota optativa - o estudante decide fazer uma prova extra para melhorar o
resultado final.
'''

notas = []

def avalia(nota_1: float, nota_2: float):

    media = (nota_1 + nota_2) / 2
    if media >= 6.0:
        print('Aprovado')
    elif 3.0 <= media < 6.0:
        print('Recuperação')
    else:
        print('Reprovado')


while True:
    for i in range(2):
        i += 1
        nota = float(input(f'Informe a {i}° nota: '))
        notas.append(nota)

    opc = input('O aluno realizou a avaliação optativa? [S/N] ')
    if opc.upper() == 'N':

        nota_1 = notas[0]
        nota_2 = notas[1]

        avalia(nota_1, nota_2)

    else:

        nota_op = float(input('Informe a nota do aluno na avaliação optativa: '))

        nota_min = min(notas)

        notas.remove(nota_min)
        notas.append(nota_op)

        n1 = notas[0]
        n2 = notas[1]
        avalia(n1, n2)

    opc = input('Deseja continuar? [S/N] ')

    if opc.upper() == 'N':
        break


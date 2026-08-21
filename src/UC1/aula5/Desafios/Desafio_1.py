'''

1. Cálculo de Média Escolar para Vários Alunos
Use o laço for para repetir a lógica de cálculo de média e status
(Aprovado/Reprovado/Recuperação) que você fez na Aula 4, agora para 10 estudantes.

'''

for x in range(10):
    for i in range(2):
        i += 1
        nota = float(input(f'Informe a {i}° nota: '))
        Desafio_5.notas.append(nota)
    opc = input('O aluno realizou a avaliação optativa? [S/N] ')
    nota_1 = Desafio_5.notas[0]
    nota_2 = Desafio_5.notas[1]

    if opc.upper() == 'S':
        nota_op = float(input('Informe a nota do aluno na avaliação optativa: '))
        nota_min = min(Desafio_5.notas)
        if nota_op > nota_min:
            Desafio_5.notas.remove(nota_min)
            Desafio_5.notas.append(nota_op)
            print('Resultado: ' + Desafio_5.avalia(nota_1, nota_2))
        else:
            print('Nota optativa menor do que as duas primeiras notas do aluno, então foi desconsiderada.')
            print('Resultado: ' + Desafio_5.avalia(nota_1, nota_2))

    elif opc.upper() == 'N':
        print('Resultado: ' + Desafio_5.avalia(nota_1, nota_2))

    else:
        print('[Erro Desconhecido!]')

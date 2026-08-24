'''
Média Escolar para 5 Estudantes
Use um for loop para iterar 5 vezes. Dentro do loop, realize a leitura das notas e a decisão
(if/elif/else) da média. Crie uma lista vazia (resultados = []). A cada repetição, adicione uma
string (ex: "Aluno 1 - Aprovado") a esta lista usando .append().
'''

resultados = []

for i in range(5):
    i = 1

    nome = input('Insira o seu nome: ')
    nota1 = float(input(f'Digite a nota do 1° bimestre:\n '))

    nota2 = float(input(f'Digite a nota do 2° bimestre:\n '))

    media = ((nota1 + nota2) / 2)

    print(media)
    if media < 0:
        print('[Nota Invalida!]')
    elif 5 <= media <= 6:
            resultados.append(f'Aluno: {nome}\n  Nota: {media}\n Resultado: Recuperação')
    elif 7 <= media <= 10:
        resultados.append(f'Aluno: {nome}\n  Nota: {media}\n Resultado: Aprovado')
    elif 5 <= media:
        resultados.append(f'Aluno: {nome}\n  Nota: {media}\n Resultado: Reprovado')

    else:
        print('[Erro Desconhecido!]')



for r in resultados:
    print('----------------------------------------')
    print(r)
    print('-----------------------------------------')



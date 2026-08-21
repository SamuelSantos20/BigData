'''

2. Cadastro de Candidatos
Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar
candidatos menores de 18 anos.
● O programa deve pedir o Ano de Nascimento do candidato.
● Se for menor de 18, o programa deve informar que ele não pode participar e pular
a coleta dos demais dados (telefone, email etc) para esse candidato.
● Se for maior de 18, o programa prossegue com o input() para os demais dados.


'''

dados = []
for i in range(1, 13):
    ano_nascimento = int(input('informe o seu ano de nascimento: '))
    idade = 2026 - ano_nascimento
    if idade > 18:
     nome = (input('Informe o seu nome:'))
     telefone = (input('Informe o telefone:'))
     email = (input('Informe o email:'))
     dados.append((ano_nascimento, nome, telefone, email))
    else :
        print('Você não pode participar desse questionario, pois você é menor de idade.')

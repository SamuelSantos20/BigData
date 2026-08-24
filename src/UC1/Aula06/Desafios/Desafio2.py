'''
Cadastro Seletivo de Candidatos
Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o
candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = [].
Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}).
Adicione este Dicionário à lista: candidatos_validos.append(candidato).
'''

candidatos_validos = []

for i in range(5):
    dataNascimento: int = int(input('Informe a sua data de nascimento: '))

    idade = 2026 - dataNascimento

    if idade > 18:
        nome = input('Informe o seu nome: ')
        email = input('Informe o seu email: ')
        telefone = input('Informe o seu telefone: ')
        candidato = {'nome': nome,
                     'email': email,
                     'telefone': telefone}

        candidatos_validos.append(candidato)
    else:
        print('Candidato invalido, pois é menor de 18 anos!')

for candidato in candidatos_validos:
    print('----------------------------------------')
    print(candidato)
    print('-----------------------------------------')
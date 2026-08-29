'''
4. Código de Origem do Produto:
Escreva um programa que leia o código de origem de um produto e imprima na tela a região
de sua procedência, conforme a tabela abaixo:
'''
while True:
    codigo = int(input('Informe o código do produto para saber sua região de origem: '))


    if codigo ==  1:
        print('SUL')
    elif codigo == 2:
        print('NORTE')
    elif codigo ==  3:
        print('Leste')
    elif codigo == 4:
        print('OESTE')
    elif codigo == 5 or codigo == 6:
        print('NORDESTE')
    elif codigo == 7 or (codigo == 8 or codigo == 9):
        print('SUDESTE')
    elif codigo == 10:
        print('CENTRO-OESTE')
    elif codigo == 11:
        print('NOROESTE')
    else:
        print('Erro de codigo')

    opc = input('Deseja continuar? [S/N] ')
    if opc.upper() == 'N':
        break





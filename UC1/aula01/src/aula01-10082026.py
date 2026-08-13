print('Olá mundo!')


#Variaveis
age:int = 21

name:str = 'Samuel Santos Miranda'

price:float = 19.0

print(age)
print(name)
print(price)

#ALgorito BOLETIM:
#nota1 = 10
#nota2 = 20
#media = (nota1 + nota2)/2
#print(media)

# Algoritmo Calculadora
operacao = 0

while operacao != 5:
    operacao = int(
        input('-----------------------Calculadora-------------------\n' + '1 - soma\n' +
              '2 - multiplicacao \n' +
              '3 - subtracao \n' +
              '4 - divisao \n' +
              '5 - Sair'+
              'Escolha uma opção:\n')
        )

    nota1 = int(input('Digite a primeira nota: '))
    nota2 = int(input('Digite a segunda nota: '))
    

    if operacao == 1:
        soma = nota1 + nota2
        print(soma)
    elif operacao == 2:
        multiplicacao = nota1 * nota2
        print(multiplicacao)
    elif operacao == 3:
        subtracao = nota1 - nota2
        print(subtracao)
    elif operacao == 4:
        divisao = nota1 / nota2
        print(divisao)
    elif operacao == 5:
        print('Saindo...')
        break



print(operacao)
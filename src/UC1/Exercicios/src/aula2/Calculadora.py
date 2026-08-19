while True  :
    print('-----------------------Calculadora-------------------\n' + '1 - soma\n' +
              '2 - multiplicacao \n' +
              '3 - subtracao \n' +
              '4 - divisao \n' +
              '5 - Sair\n')

    operacao = int(input('Escolha uma opção:\n'))

    if operacao > 5:
        print("Opção invalida!")

    else:
        nota1 = int(input('Digite a primeira nota: '))
        nota2 = int(input('Digite a segunda nota: '))

        match operacao:
            case 1:
                soma = nota1 + nota2
                print(soma)
            case 2:
                multiplicacao = nota1 * nota2
                print(multiplicacao)
            case 3:
                subtracao = nota1 - nota2
                print(subtracao)
            case 4:
                divisao = nota1 / nota2
                print(divisao)
            case 5:
                sair = 'Saindo do sistema...'
                print(sair)
                break



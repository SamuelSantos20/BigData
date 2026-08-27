def calculadora(num1:int, num2:int, opc:int) -> str | None:
    match opc:
        case 1:
            return f'Resultado da operação: {num1 + num2}'
        case 2:
            return f'Resultado da operação: {num1 - num2}'
        case 3:
            return f'Resultado da operação: {num1 * num2}'
        case 4:
            if opc != 0:
                return f'Resultado da operação: {num1 / num2}'
            else:
                return 'Não é possivel calcular divião por zero.'


while True:
    opc = int(
        input('-----------------------------\nInforme a opção desejada:\n (1) -adição\n (2) -subtração \n (3) - multiplicação \n (4) - divisão\n (5) - Sair do programa.\n-------------------------------------\n'))

    if opc == 5:
        break
    else:
        num1 = int(input('Digite o primeiro numero: '))

        num2 = int(input('Digite o segundo numero: '))

        print(calculadora(num1, num2, opc))


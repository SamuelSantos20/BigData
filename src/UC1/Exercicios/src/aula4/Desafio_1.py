'''
1. Cálculo de Lâmpadas:
Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
3m² existe um bocal para uma lâmpada.
'''
while True:

    l = int(input("Informe a Largura do comodo em metros: "))

    c = int(input("Informe a comprimento do comodo em metros: "))

    m = l * c

    soma = 0
    cont = 0
    while soma < m:
        cont += 1

        soma += 3

    print(f"Seriam necessaria {cont} lâmpadas para acender um comodo de {m}m²")

    opc = input("Deseja continuar? [S/N] ")
    if opc.upper() == "N":
        break




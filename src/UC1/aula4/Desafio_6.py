'''
6. Positivo ou Negativo:
Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o
valor zero como positivo.
'''

while True:

    number = int(input('Digite um valor para saber se ele é positivo ou negativo: '))

    if number >=0:
        print("Numero Positivo")

    else:
        print("Numero Negativo")


    opc = input("Deseja Continuar? [S/N] ")

    if opc.upper() == "N":
        break


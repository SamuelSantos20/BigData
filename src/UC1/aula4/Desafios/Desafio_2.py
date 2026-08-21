'''
2. Quantidade de Caixas de Azulejos:
Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
todas as suas paredes (considere que não será descontada a área ocupada por portas e
janelas). Cada caixa de azulejos possui 1,5 m²
'''
while True:
    cumprimento = float(input("Informe o comprimento da cozinha (em metros): "))
    largura =   float(input("Informe a largura da cozinha (em metros): "))
    altura = float(input("Informe a altura da cozinha (em metros): "))


    are_paredes = (2 * cumprimento * altura) + (2* largura * altura)

    quantidade_caixas = are_paredes / 1.5


    print(f"\nArea total das paredes: {are_paredes:.2f}m²")

    print(f"Quantidade necessarios: {quantidade_caixas:.2f} caixas de azulejos")

    opc = input("Deseja continuar? [S/N] ")

    if opc.upper() == "N":
        break
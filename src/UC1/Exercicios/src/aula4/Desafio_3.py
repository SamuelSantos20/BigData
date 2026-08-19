'''
3. Rendimento do Taxista:
Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
média do consumo em km/L e o lucro (líquido) do dia.
'''


VALOR_COMBUSTIVEL = 6.15

km_init = float(input("Informe a marcação do andometro no inicio do dia: "))

km_fin = float(input("Informe a marcação do andometro no final do dia: "))

litros = int(input('informe a quantidade gasta de litros: '))

value_pass = float(input("Informe o valor total recebido pelos passageiros: "))


km_r = km_fin - km_init

km_l = km_r/litros

gasto = litros * VALOR_COMBUSTIVEL

lucro = value_pass - gasto


print(f'A média de km/l foi de {km_l:.2f} e o lucro foi de {lucro:.2f}')






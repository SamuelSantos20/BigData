'''
1. Controle de Pesca
Crie um programa que ajude um pescador a controlar sua produtividade. Toda vez que ele
traz um peso de peixes maior que o estabelecido pelo regulamento (100 quilos), ele deve
pagar uma multa de R$ 4,00 por quilo excedente.
● O programa deve ler o peso de peixes (em quilos) pescado no dia.
● Você deve criar uma função (ex: calcular_multa(peso_total)) que recebe o peso e
retorna o valor da multa (que pode ser 0.0 se estiver dentro do limite).
● Se o valor da multa retornado for maior que zero, mostre a multa.
● Caso contrário, mostre a mensagem "Peso dentro do limite. Nenhuma multa a
pagar."
● Pergunte o peso de várias pescarias feitas ao longo da semana. O loop para quando
o usuário digitar 0. Ao final, mostre o total de multa acumulado no dia.
'''


def calcular_multa(peso_total:float) -> float | str:
    if peso_total > 100 :
        multa = (peso_total - 100) * 4
        return f"A multa total é de = {multa}\n"
    else:
        return 'Peso dentro do limite. Nenhuma multa apagar.\n'



def chat():
    while True:

        quantidade_kg = float(input('Informe a quantidade em kg de pescares: \n'))

        print(calcular_multa(quantidade_kg))

        opc = int(input('Pressione 0 para sair ou 1 para continuar e clique em <enter>:\n'))


        if opc == 0:
            break
        elif opc != 1:
            while opc != 1:
                print('Opção invalida!!')
                opc = int(input('Pressione 1 para continuar ou 0 para sair.\n'))



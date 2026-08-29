#FUNÇÕES E MODULOS

# SORTEIO DE NUMEROS:

import random

numero_random = random.randint(1,30)

print(numero_random)


def sorteiame()-> int:
    '''
    Algoritimo escolhe e retorna um numero inteiro aleatorio no intervalo e 1 a 30
    :return:
    '''
    numero_sorteado = random.randint(1,30)

    return numero_sorteado


print(sorteiame())
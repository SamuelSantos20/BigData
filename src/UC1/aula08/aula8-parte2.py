import time

def dar_boas_vindas():
    print('-'*40)
    print('Bem indo ao nosso aplicativo! 😀')
    print('-' * 40)

# 2. CHAMADA DA FUNÇÃO
# O código abaixo só será executado se você "chamar" a função pelo nome

print('Incio do programa...')
print('Por favor, aguarde...')

time.sleep(2) # simula uma pausa

dar_boas_vindas()# <--- isso executa o código dentro da função

print('Meio do programa...')
dar_boas_vindas()# <--- Podemos chamar de novo

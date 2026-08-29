'''
3. Tentativa de Login e Senha
Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
para digitar a senha correta.
● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
● Dê ao usuário 3 tentativas para acertar a combinação.
● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
break para sair do loop.
● Se a senha estiver errada, informe o erro e diminua o número de tentativas
restantes.
● Se as tentativas acabarem, imprima uma mensagem de bloqueio.
'''



usuario_salvo = 'admin'
senha_salva = '123456'

cont = 0
for i in range(3):
    cont += 1
    usuario = (input('Digite o seu usuario: '))
    senha = (input('Digite sua senha: '))

    if usuario == usuario_salvo and senha == senha_salva:
        print('Usuario e senha corretos!')
        break
    else:
        print('Usuario ou senha incorretos.')
if cont > 3:
    print('Numeros de tentativas excedidas!')
    print('Sua conta está temporariamente bloqueada!')
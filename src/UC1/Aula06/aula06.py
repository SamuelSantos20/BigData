# # dados = ['Samuel','Juan',1236,True,68.40,[10,5,6,8]]
# #
# # print(dados[5])
# #
# # print(dados[3])
# #
# # print(dados[5][2])
# #
# #
# # participantes = ['Paulo','Angela','Antonio','Andre',]
# # for participante in participantes:
# #     print(participante)
# #
# #
# #
#
# participantes = ('Paulo','Angela','Antonio','Andre')
#
# print(participantes,type(participantes))
#
#
# #Tuplas
#
# nomes = ('Samuel','Jose','Antonio')
# print(nomes,type(nomes))
#
# lista_nomes  = list (nomes)
#
#
#
# print(lista_nomes,type(lista_nomes))
#
#
# #Sets
# numeros_pares = {202,
#                 203,
#                 204,
#                 204,
#                 205,
#                 219,
#                 291,
#                 292,
#                 202}
#
#
# # print(nmeros_pares,type(nmeros_pares))
#
#
# numeros_impares = {111,111,112,291,291,205}
#
# print(numeros_pares.intersection(numeros_impares))
# numeros_pares.remove(205)
# print(numeros_pares)
# # print(numeros_impares,type(numeros_impares))


#Dicionarios:
produtos = {
    'maça':5.99,
    'laranja':4.79
}

print(produtos, type(produtos))

print(produtos.items())

print(produtos.keys())

print(produtos.values())

print(produtos.get('laranja'))
#produtos.update("laranja")


produtos2 = produtos.copy()

print(produtos2)
produtos.update()

#produtos.pop('maça')

produtos2["maça"] = 7.99

print(produtos2)

###

achadinhos = {}

achadinhos['capinha de celular'] = 12.99
print(type(achadinhos))


from operator import index

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl as xl


numeros_impares = [43,55,1,3,11,27,109]

numeros_seq = [2,3,4,5,6,6,7]

serie_impares = pd.Series(numeros_impares)

#print(serie_impares)
#print(type(serie_impares))

print(serie_impares.sum())

#print(serie_impares.mean())

#print(serie_impares.min())

#print(serie_impares.max())

#print(len(serie_impares))


#print(serie_impares.describe())

#print(serie_impares[serie_impares>50])


#serie2_impares = pd.Series(numeros_impares, index = ['a','b','c','d','e','f','g'])
#print(serie2_impares)

#print(serie2_impares)


#serie_imparesQ = serie_impares * serie_impares

#print(serie_imparesQ)


'''filmes = {
    'nome': ['Lagoa Azul', 'Agente Secreto','Gênio Indomavel'],
    'categoria': ['Romance','Ação','Drama'],
    'ano': ['1980','2025','1997'],
    'faturamento': []
}
'''
'''tabela_filmes = pd.DataFrame(filmes)

print(filmes)
print(type(filmes))
print(tabela_filmes)
print(type(tabela_filmes))

'''
### LEITURA DE XLSX

leitura_invest = pd.read_excel('base_invest.xlsx',1)

print(leitura_invest)

filmes = {
    'nome': ['Lagoa Azul', 'Agente Secreto','Gênio Indomavel','A freira','Sexta feira 13', 'Top Guun'],
    'categoria': ['Romance','Ação','Drama','Terror','Terror','Aventura'],
    'ano': ['1980','2025','1997','2014','1990','1986'],
    'faturamento': [6.0,5.0,5.5,8.0,6.8,7.0]
}

tabela_filmes = pd.DataFrame(filmes)

print(filmes)
print(type(filmes))
print(tabela_filmes)
print(type(tabela_filmes))

print(tabela_filmes.iloc[-1])

indices = ['A','B','C','D','E','F']


tabela_filmes = pd.DataFrame(filmes, index = indices)

print(tabela_filmes)


print(tabela_filmes.loc['B'])
print(tabela_filmes.iloc[1:3])

print(tabela_filmes.query('ano == 1995'))
#print('-'*20)
#print(tabela_filmes.loc['titulo'])
#print('-'*20)
#print(tabela_filmes.loc['titulo'] != 'Agente Secreto')
#print('-'*20)

consulta1 = tabela_filmes.query('faturamento == 5.5')

print(consulta1)
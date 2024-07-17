import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
  
def pergunta1(df):
    dfCategory = df[df['Categoria'] == 'Office Supplies']
    agrupamento = dfCategory.groupby('Cidade')['Valor_Venda'].sum().reset_index()
    maiorVenda = agrupamento.loc[agrupamento['Valor_Venda'].idxmax()]
    print('Resposta da Pergunta 1:')
    print(maiorVenda)
    
df = pd.read_csv('dataset.csv')
# data = pd.read_csv('dataset.csv')
'''
exploração de dados (busca de possíveis dados errados[errados ou duplicados])

print(df[df.duplicated()])
print(df.isnull().sum())
'''

# pergunta1(data)

df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format='%d/%m/%Y')
agrupamento = df.groupby('Data_Pedido')['Valor_Venda'].sum().reset_index()
print(agrupamento)
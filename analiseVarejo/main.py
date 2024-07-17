import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
  
def pergunta1(df):
    #filtrando coluna
    dfCategory = df[df['Categoria'] == 'Office Supplies']
    
    #somando coluna e procura o indice do maior valor
    agrupamento = dfCategory.groupby('Cidade')['Valor_Venda'].sum().reset_index()
    maiorVenda = agrupamento.loc[agrupamento['Valor_Venda'].idxmax()]
    print('Resposta da Pergunta 1:')
    print(maiorVenda)

def pergunta2(df):
    #filtrando dados
    df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], format='%d/%m/%Y')
    agrupamento = df.groupby('Data_Pedido')['Valor_Venda'].sum().reset_index()

    #plotando dados
    plt.figure(figsize=(12, 8))
    plt.bar(agrupamento['Data_Pedido'], agrupamento['Valor_Venda'], color='green')
    plt.title('Total de Vendas por Data')
    plt.xlabel('Data do Pedido')
    plt.xticks(rotation=45) #melhor visualização
    plt.ylabel('Valor total ($)')
    plt.grid(True)
    plt.tight_layout()

    plt.show() 

def pergunta3(df):
    #filtra os dados
    agrupamento = df.groupby('Estado')['Valor_Venda'].sum().reset_index()

    #plota os dados
    plt.figure(figsize=(18, 5))
    plt.bar(agrupamento['Estado'], agrupamento['Valor_Venda'], color='green')
    plt.title('Total de Vendas por Data')
    plt.xlabel('Estado')
    plt.xticks(rotation=90) #melhor visualização
    plt.ylabel('Valor total ($)')
    plt.grid(axis='y')
    plt.tight_layout()

    plt.show()

#df = pd.read_csv('dataset.csv')
data = pd.read_csv('dataset.csv')
'''
exploração de dados (busca de possíveis dados errados[errados ou duplicados])

print(df[df.duplicated()])
print(df.isnull().sum())
'''

# pergunta1(data)
# pergunta2(data)
pergunta3(data)

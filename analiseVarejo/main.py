import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# Pergunta de Negócio 1: Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?  
def pergunta1(df1):
    #filtrando coluna
    dfCategory = df1[df1['Categoria'] == 'Office Supplies']
    
    #somando coluna e procura o indice do maior valor
    agrupamento = dfCategory.groupby('Cidade')['Valor_Venda'].sum().reset_index()
    maiorVenda = agrupamento.loc[agrupamento['Valor_Venda'].idxmax()]
    print('Resposta da Pergunta 1:')
    print(maiorVenda)

# Pergunta de Negócio 2: Qual o Total de Vendas Por Data do Pedido?
# Demonstre o resultado através de um gráfico de barras.
def pergunta2(df2):
    #filtrando dados
    df2['Data_Pedido'] = pd.to_datetime(df2['Data_Pedido'], format='%d/%m/%Y')
    agrupamento = df2.groupby('Data_Pedido')['Valor_Venda'].sum().reset_index()

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

# Pergunta de Negócio 3: Qual o Total de Vendas por Estado?
# Demonstre o resultado através de um gráfico de barras.
def pergunta3(df3):
    #filtra os dados
    agrupamento = df3.groupby('Estado')['Valor_Venda'].sum().reset_index()

    #plota os dados
    plt.figure(figsize=(18, 5))
    plt.bar(agrupamento['Estado'], agrupamento['Valor_Venda'], color='green')
    plt.title('Total de Vendas por Estado')
    plt.xlabel('Estado')
    plt.xticks(rotation=90) #melhor visualização
    plt.ylabel('Valor total ($)')
    plt.grid(axis='y')
    plt.tight_layout()

    plt.show()

#Pergunta de Negócio 4: Quais São as 10 Cidades com Maior Total de Vendas?
def pergunta4(df4):
    #selecionando o agrupamento e selecionando os 10 maiores [ordenando e usando os 10 primerios]
    agrupamento = df4.groupby('Cidade')['Valor_Venda'].sum().reset_index()
    maiores_vendas = agrupamento.sort_values(by='Valor_Venda', ascending=False).head(10)

    #plotando o grafico de barras
    plt.figure(figsize=(11, 8))
    plt.bar(maiores_vendas['Cidade'], maiores_vendas['Valor_Venda'], width=0.5, color='green')
    plt.title('Top 10 cidades com maiores vendas')
    plt.xlabel('Cidade')
    plt.xticks(rotation=45) #melhor visualização
    plt.ylabel('Valor total ($)')
    plt.grid(axis='y')

    plt.show()

# Pergunta de Negócio 5: Qual Segmento Teve o Maior Total de Vendas?
# Demonstre o resultado através de um gráfico de pizza.
def pergunta5(df5):
    #dividindo o agrupamento e ordenando para melhor vizualização
    agrupamento = df5.groupby('Segmento')['Valor_Venda'].sum().reset_index()
    pie = agrupamento.sort_values(by='Valor_Venda', ascending=False).head(3)
    
    # variaveis do grafico
    labels = pie['Segmento']
    sizes = pie['Valor_Venda']
    colors = ['gold', 'yellowgreen', 'lightcoral']
    explode = (0.1, 0, 0)

    # construindo grafico
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')
    plt.title('Venda por segmento')

    plt.show()   

# Pergunta de Negócio 6 (Desafio Nível Baby): Qual o Total de Vendas Por Segmento e Por Ano?
def pergunta6(df6):
    #determina o formato para dia mes e ano
    df6['Data_Pedido'] = pd.to_datetime(df6['Data_Pedido'], format='%d/%m/%Y')

    # usa a função assign para criar uma coluna apenas em tempo de execução e capturar seus valores
    agrupamento = (
        df6
        .assign(Ano= lambda x: x['Data_Pedido'].dt.year)
        .groupby(['Ano', 'Segmento'])['Valor_Venda']
        .sum()
        .reset_index()
    )

    print("Resposta da pergunta 6:")
    print(agrupamento.head(9))

# Pergunta de Negócio 7 (Desafio Nível Júnior): Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
# Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
# Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
# Quantas Vendas Receberiam 15% de Desconto?
def pergunta7(df7):
    #query para verificar se o valor é maior que 1000
    elegivel_desconto = df7.query('Valor_Venda > 1000')
    
    #usando função shape para contar quantas linhas tem o valor > 1000
    print(f'\tNúmero de vendas elegíveis ao desconto de 15%: {elegivel_desconto.shape[0]}\n')
    print(elegivel_desconto.head())

#Pergunta de Negócio 8 (Desafio Nível Master): Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?
def pergunta8(df8):
    #calculo da média geral
    print(df8.describe())
    media_geral = df8['Valor_Venda'].mean()
    
    #calculo da media dando 15% de desconto em vendas com valor > 1000
    media_desconto_15 = df8.assign(
        Valor_Desconto = lambda x: x['Valor_Venda'].apply(lambda valor: (valor * 0.85) if valor > 1000 else valor)
    )['Valor_Desconto'].mean()
    
    #calculo da media dando 15% de desconto em vendas com valor > 1000 e desconto de 10% em vendas com valor < 1000
    media_desconto_total = df8.assign(
        Valor_Desconto = lambda x: x['Valor_Venda'].apply(lambda valor: (valor * 0.85) if valor > 1000 else (valor * 0.9))
    )['Valor_Desconto'].mean()

    print(f'Media de valores de venda originais: {round(media_geral, 2)}\nMedia de valores com descontos de 15%: {round(media_desconto_15, 2)}\nMedia de valores com todos descontos: {round(media_desconto_total, 2)}')

# Pergunta de Negócio 9 (Desafio Nível Master Ninja): Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
# Demonstre o resultado através de gráfico de linha.
def pergunta9(df9):
    #usa o datetime para formatar a data
    df9['Data_Pedido'] = pd.to_datetime(df9['Data_Pedido'], format='%d/%m/%Y')

    #faz o agrupamento usando o mes e o ano, e em sequencia soma o valor total do agrupamento
    agrupamento_mes_ano_segmento = (
        df9
        .assign(
            Ano = lambda x: x['Data_Pedido'].dt.year,
            Mes = lambda x: x['Data_Pedido'].dt.month
        )  
        .groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda']
        .sum()
        .reset_index()
    )

    # cria uma nova coluna pra ficar mais facil de plotar o gráfico
    '''obs usei o rename pq estava com erro no nome das colunas'''
    agrupamento_mes_ano_segmento['Ano_Mes'] = pd.to_datetime(agrupamento_mes_ano_segmento[['Ano', 'Mes']].rename(columns={'Ano': 'year', 'Mes': 'month'}).assign(Day=1))

    plt.figure(figsize=(14, 8))

    # fazendo uma linha para cada segmento(3)
    for segmento in agrupamento_mes_ano_segmento['Segmento'].unique():
        dados_segmento = agrupamento_mes_ano_segmento[agrupamento_mes_ano_segmento['Segmento'] == segmento]
        plt.plot(dados_segmento['Ano_Mes'], dados_segmento['Valor_Venda'], marker='o', label=segmento)

    # plotando grafico
    plt.title('Total de Vendas por Ano, Mês e Segmento')
    plt.xlabel('Ano e Mes')
    plt.ylabel('Total de Vendas ($)')
    plt.legend(title='Segmento')
    plt.grid(True)
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

# Pergunta de Negócio 10 (Desafio Nível Master Ninja das Galáxias): Qual o Total de Vendas Por Categoria e SubCategoria, Considerando Somente as Top 12 SubCategorias?
# Demonstre tudo através de um único gráfico.
def pergunta10(df10):
    
    # fazendo agrupamento com categoria e sub categoria, e somando o valor total
    agrupamento = df10.groupby(['Categoria', 'SubCategoria'])['Valor_Venda'].sum().reset_index()
    # ordenando em ordem decrescente e pegando os 10 primerios valores
    maiores_vendas = agrupamento.sort_values(by='Valor_Venda', ascending=False).head(12)

    plt.figure(figsize=(14, 8))
    
    #plotando brafico de barras da horizontal
    plt.barh(
        y = maiores_vendas.apply(lambda row: f"{row['Categoria']}: {row['SubCategoria']}", axis=1),
        width = maiores_vendas['Valor_Venda'],
        color = 'green'
    )

    plt.title('Top 12 Maiores Vendas por Categoria e SubCategoria')
    plt.xlabel('Valor de Venda ($)')
    plt.ylabel('Categoria - SubCategoria')
    plt.gca().invert_yaxis()
    plt.grid(axis='x', linestyle='--')

    plt.tight_layout()
    plt.show()

data = pd.read_csv('dataset.csv')

'''
exploração de dados (busca de possíveis dados errados[errados ou duplicados])

print(df[df.duplicated()])
print(df.isnull().sum())
'''

pergunta1(data)
pergunta2(data)
pergunta3(data)
pergunta4(data)
pergunta5(data)
pergunta6(data)
pergunta7(data)
pergunta8(data)
pergunta9(data)
pergunta10(data)

print('Fim do Projeto')
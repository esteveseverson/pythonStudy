import pandas as pd

'''
Codigo que usei para adaptar o CSV do INMET com as temperaturas de Interlagos em São Paulo.

Ele consulta o CSV diposnivel no site: https://portal.inmet.gov.br/dadoshistoricos (escolhi por opção 2023 SP intergalos)
Pega a coluna da data, faz uma média da temperatura da hora e em seguida faz uma media da temperatura do dia (reduzindo de 8000 colunas para 365 [para fins didaticos])
'''

# Carregar o CSV com a codificação 'latin1'
df = pd.read_csv('analiseDadosTemperatura/INMET_SE_SP_A771_SAO PAULO - INTERLAGOS_01-01-2023_A_31-12-2023.CSV', sep=';', skiprows=8, encoding='latin1')

# Selecionar as colunas desejadas
selected_columns = df[['Data', 'TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)', 'TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)']]

# Substituir vírgulas por pontos e converter as colunas para float
selected_columns['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'] = selected_columns['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'].str.replace(',', '.').astype(float)
selected_columns['TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)'] = selected_columns['TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)'].str.replace(',', '.').astype(float)

# Calcular a média dessas colunas para cada linha
selected_columns['TEMPERATURA MEDIA (°C)'] = selected_columns[['TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)', 'TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)']].mean(axis=1)

# Agrupar por 'Data' e calcular a média diária
daily_mean = selected_columns.groupby('Data')['TEMPERATURA MEDIA (°C)'].mean().reset_index()

# Salvar o resultado em um novo arquivo CSV
daily_mean.to_csv('temperatura_media_diaria.csv', index=False)
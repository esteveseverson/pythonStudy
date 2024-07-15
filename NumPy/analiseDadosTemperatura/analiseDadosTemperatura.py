import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Gerar 365 temperaturas aleatórias entre 2 e 35 (pesquisei a menor e a maior temperatura de MG em 2024)
# Tirei cerca de 10% dos valores para fazer a interpolação de dados faltantes

'''
durante a fabricaçção do código, eu usava arrays aleatorios para fazer o teste
def gerarTemperaturasAleatorias():
    randArray = np.random.uniform(2, 35, 366)
    missingValues = np.random.randint(0, 366, 36)
    for x in missingValues:
        randArray[x] = np.nan
    return randArray
'''

def temperatureGen():
    df = pd.read_csv('analiseDadosTemperatura/temperatura_media_diaria.csv')
    array = df['TEMPERATURA MEDIA (°C)'].to_numpy()
    
    #para a interpolação dos dados, excluirei propositalmente mais ou menos 10% dos dados
    missingValues = np.random.randint(0, 365, 36)
    for x in missingValues:
        array[x] = np.nan
    
    return array

#Faz o calculo de valores estatisticos do array gerado, desconsiderando os valores np.nan
def printStatistical(randomArray):
    result = [np.nanmean(randomArray), np.nanmedian(randomArray), np.nanstd(randomArray), np.nanvar(randomArray)]
    menor, maior = temperaturePeaks(randomArray)
    
    output = f"""
| {'Estatística':<20} | {'Valor':<10} |
|----------------------|------------|
| {'Média':<16}     | {result[0]:.2f}{'':<5} |
| {'Mediana':<18}   | {result[1]:.2f}{'':<5} |
| {'Desvio Padrão':<20} | {result[2]:.2f}{'':<6} |
| {'Variância':<20} | {result[3]:.2f}{'':<5} |
| {'Menor Temperatura':<15}    | {menor:.2f}{'':<5} |
| {'Maior Temperatura':<15}    | {maior:.2f}{'':<5} |
"""
    print(output)

#Interpolação de dados, método linear
def linearInterpole(randomArray):
    
    #Indices dos valores validos
    linear = np.copy(randomArray)
    indices_validos = np.arange(len(linear))
    mascara_validos = ~np.isnan(linear)

    # indices e valores validos
    indices = indices_validos[mascara_validos]
    dados = linear[mascara_validos]

    #indices que estão nulos
    indices_nan = indices_validos[np.isnan(linear)]

    #interpolando os dados
    linear[np.isnan(linear)] = np.interp(indices_nan, indices, dados)
    return linear

def polinomialInterpole(randomArray):
    # indices dos valores validos
    polinomial = np.copy(randomArray)
    indices_validos = np.arange(len(polinomial))
    mascara_validos = ~np.isnan(polinomial)

    # indices e valores validos
    indices = indices_validos[mascara_validos]
    dados = polinomial[mascara_validos]

    # grau do polinomio para verificação
    grau = 2
    coeficiente_polinomio = np.polyfit(indices, dados, grau)

    #indices que estão nulos
    indices_nan = indices_validos[np.isnan(polinomial)]

    #interpolando os dados
    polinomial[np.isnan(polinomial)] = np.polyval(coeficiente_polinomio, indices_nan)
    return polinomial

def temperaturePeaks(randomArray):
    menorTemperatura = 100
    maiorTemperatura = 0
    for x in range (0, len(randomArray), 1):
        if menorTemperatura > randomArray[x]:
            menorTemperatura = randomArray[x]
        if maiorTemperatura < randomArray[x]:
            maiorTemperatura = randomArray[x]
    
    return menorTemperatura, maiorTemperatura

def dataView(array, interp, polinomial):
    # x = numero de dados
    x = np.arange(365)
    
    # dados do grafico
    plt.figure(figsize=(17, 10))
    plt.plot(x, array, label="Array Original", color="blue", marker="o")
    plt.plot(x, interp, label="Interp. Linear", color="green", linestyle="--")
    plt.plot(x, polinomial, label="Interp. Polinomial", color="red", linestyle="--")

    # titulos e rótulos
    plt.title("Gráficos de temperaturas durante 365 dias")
    plt.xlabel("Dias")
    plt.ylabel("Temperatura (°C)")

    # grade e legenda
    plt.grid(True)
    plt.legend()

    plt.show()

arrayTemperature = temperatureGen()
linearInterpTemperature = linearInterpole(arrayTemperature)
polinomialInterpTemperature = polinomialInterpole(arrayTemperature)

print("• TEMPERATURAS COM VALORES NULOS:", end="")
printStatistical(arrayTemperature)
print("• TEMPERATURAS COM INTERPOLAÇÃO LINEAR:", end="")
printStatistical(linearInterpTemperature)
print("• TEMPERATURAS COM INTERPOLAÇÃO POLINOMIAL:", end="")
printStatistical(polinomialInterpTemperature)

dataView(arrayTemperature, linearInterpTemperature, polinomialInterpTemperature)
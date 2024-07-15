'''
meu primeiro codigo

import numpy as arr
import random

def randomArrayGen():
    vet = arr.array(arr.zeros(101), dtype= arr.int16)
    coin = [0,1] # 0 = cara 1 - coroa
    for i in range (0,101):
        vet[i] = random.choice(coin)
        
    return vet
    
def percentageCalc(vet):
    #print(f'A media foi {round(arr.mean(randomArrayGen()),5)}')
    if arr.mean(vet) > 0.5:
        print("O número de vezes que 'coroa' apareceu foi maior")
    elif arr.mean(vet) < 0.5:
        print("O numero de vezes que 'cara' apareceu foi maior")
    elif arr.mean(vet) == 0.5:
        print("O numero de vezes entre 'cara' e 'coroa' foi exatamente igual")
    
vet = randomArrayGen()
percentageCalc(vet)
'''

#codigo mais focado em numpy

import numpy as np

def randomArrayGen():
    # Cria um array com 101 elementos usando np.random.choice
    vet = np.random.choice([0, 1], size=101)
    return vet

def percentageCalc(vet):
    # Calcula a média do array
    mean_val = np.mean(vet)
    if mean_val > 0.5:
        print("O número de vezes que 'coroa' apareceu foi maior")
    elif mean_val < 0.5:
        print("O número de vezes que 'cara' apareceu foi maior")
    else:
        print("O número de vezes entre 'cara' e 'coroa' foi exatamente igual")

# Gera o array e calcula a porcentagem
vet = randomArrayGen()
contCara, contCoroa = 0, 0
for i in vet:
    if i == 0:
        contCara += 1
    elif i == 1:
        contCoroa += 1

print(f"O lado cara foi sorteado {contCara} vezes\nO lado coroa foi sorteado {contCoroa} vezes")
percentageCalc(vet)

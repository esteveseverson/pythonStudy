import numpy as np

def randomListGen():
    return np.random.randint(0, 101, 11)

def statisticalCalc(randomList):
    return np.mean(randomList), np.median(randomList), np.std(randomList), np.var(randomList)

randomList = randomListGen()
statOps = statisticalCalc(randomList)
print(randomList)
print(f"A média é {statOps[0]}\nA mediana é {statOps[1]}\nO desvio padrão(sqrt(var)) é {round(statOps[2], 2)}\nE a variância foi {round(statOps[3], 2)}")

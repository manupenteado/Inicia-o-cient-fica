import numpy as np
import matplotlib.pyplot as plt

#definindo uma função para trabalharmos:
#y em função de x
def funcao_y(x):
    return np.sin(x)

def derivada_y(x):
    return np.cos(x)

#vai de -5 a 5 com um passo de 0.1
x = np.arange(-5, 5, 0.1)
y = funcao_y(x)

#um ponto
posicao_atual = (1.5, funcao_y(1.5))

taxa_aprendizagem = 0.01

for _ in range (1000):
    novo_x = posicao_atual[0] - taxa_aprendizagem * derivada_y(posicao_atual[0])
    novo_y = funcao_y(novo_x)
    posicao_atual = (novo_x, novo_y)
    
    plt.plot(x, y)
    plt.scatter(posicao_atual[0], posicao_atual[1], color = "red")
    plt.pause(0.0001)
    plt.clf()

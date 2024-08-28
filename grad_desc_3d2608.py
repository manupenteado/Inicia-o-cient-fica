import numpy as np
import matplotlib.pyplot as plt 


def funcao_z(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5

#derivada e vai entrar derivada parcial nisso ai
#O gradiente de uma função de duas variáveis, 
# 𝑓(𝑥,𝑦)f(x,y), é um vetor que contém ambas as derivadas parciais
def calular_gradiente(x, y):
    #essa função retorna 2 valores, sendo o primeiro 
    #a derivada parcial em relação a x e o segundo a derivada parcial
    #em relação a y
    return np.cos(5 * x) * np.cos (5 * y), -np.sin(5 * x) * np.sin (5 * y)

x = np.arange (-1, 1, 0.05)
y = np.arange (-1, 1, 0.05)

#Esta função cria duas matrizes 2D a partir dos vetores x e y fornecidos. 
# É usada para gerar coordenadas de grade para 
# funções de duas variáveis.
X, Y = np.meshgrid(x, y)

#Se você tentar calcular Z = funcao_z(x, y) diretamente sem usar np.meshgrid,
#  o resultado não será o mesmo que com meshgrid, porque x e y 
# serão apenas vetores e não coordenadas em uma grade.
#A função funcao_z seria aplicada element-wise (por elemento) 
# se funcao_z suportar operações vetoriais.
#é um padrão usar letra maiuscula para matrizes
Z = funcao_z (X, Y)

pos_atual = (0.7, 0.4, funcao_z(0.7, 0.4))
taxa_aprendizagem = 0.01

#ax é uma variavel que recebe o objeto 3d criado
#computed_zorder = False -> para conseguir enxergar o ponto, porque a função é sempre priorizada
ax = plt.subplot(projection = "3d", computed_zorder = False)

for _ in range (100):
    derivada_x, derivada_y = calular_gradiente(pos_atual[0], pos_atual[1])
    novo_x, novo_y = pos_atual[0] - taxa_aprendizagem * derivada_x, pos_atual[1] - taxa_aprendizagem * derivada_y
    pos_atual = (novo_x, novo_y, funcao_z(novo_x, novo_y))

    ax.plot_surface(X, Y, Z, cmap = "viridis", zorder = 0)
    ax.scatter(pos_atual[0], pos_atual[1], pos_atual[2], color = "magenta", zorder = 1)
    plt.pause(0.001)
    ax.clear()


print("oi")


import numpy as np
import matplotlib.pyplot as plt 

#definindo a função
def funcao_z(x, y):
    return ((1 - x)**2) + (100 * (y - (x**2))**2)

#calculando as derivadas parciais
def calular_gradiente(x, y):
    return ((-2) * (1 - x)) - (400 * x * (y - x**2)), 200 * (y - x**2)

#definindo valores para construção do gráfico
x = np.arange (-2, 2, 0.1)
y = np.arange (-1, 3, 0.1)

#criando duas matrizes 2D a partir dos vetores x e y
X, Y = np.meshgrid(x, y)

#definindo uma variavel para a função f(x,y)
Z = funcao_z (X, Y)

#definindo um ponto inicial
pos_atual = (0, 0, funcao_z(0, 0))

#definindo a taxa de aprendizagem
taxa_aprendizagem = 0.001

#ax é uma variavel que recebe o objeto 3d criado
#computed_zorder = False -> para conseguir enxergar o ponto, porque sem ele a função é sempre priorizada
#zorder funciona em ordem, definindo a prioridade dos desenhos
ax = plt.subplot(projection = "3d", computed_zorder = False)

#o loop vai se repetir 1000x
#quanto maior o número de repetições, mais perto do mínimo real vai se chegar
for _ in range (1000):

    #recebendo os valores da derivadas correspondentes a cada ponto
    vetor_grade = calular_gradiente(pos_atual[0], pos_atual[1])
    derivada_x = vetor_grade[0]
    derivada_y = vetor_grade[1]

    #se o vetor gradiente (que contem as derivadas) for muito pequeno, ocorre a interrupçao
    if np.linalg.norm(vetor_grade) < 1e-6:
        break

    #se o vetor gradiente for maior que 10**-6, o x e y vao assumir novos valores
    #se aproximam do ponto minimo atravez do produto entre a taxa de aprendizagem e a posicao atual
    novo_x, novo_y = pos_atual[0] - taxa_aprendizagem * derivada_x, pos_atual[1] - taxa_aprendizagem * derivada_y
    pos_atual = (novo_x, novo_y, funcao_z(novo_x, novo_y))

    #criando o gráfico
    ax.plot_surface(X, Y, Z, cmap = "plasma", zorder = 0)
    ax.scatter(pos_atual[0], pos_atual[1], pos_atual[2], color = "blue", zorder = 1)
    plt.pause(0.001)
    ax.clear()

    #fim do for

#pegando os ultimos valores de x e y (os valores minimos calculados) e arredondando para 4 casas decimais
x_minimo = round (novo_x, 4)
y_minimo = round (novo_y, 4)

print(f"O mínimo global da função é aproximadamente em = ({x_minimo}, {y_minimo})")


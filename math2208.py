import numpy as np
import matplotlib.pyplot as plt

#funcao de x que depende de x
#o grafico da função é uma parabola e queremos achar o minimo dessa função
def funcao_y(x):
    return x**2

#para achar o minimo, precisamos computar a derivada da função
#o que é derivada de uma função? é a inclinação (slope) da reta tangente no ponto

def derivada_y(x):
    return 2 * x

#gerando alguns valores
#começa em -100, vai até 100, com um "passo" de 0.1
x = np.arange(-100, 100, 0.1)

#como y depende de x, os valores de y serão x^2 e eles são definidos pela função que criamos em função de x:
y = funcao_y(x)

#precisamos definir um ponto de inicio para que os testes comecem
posicao_atual = (80, funcao_y(80))

#essa função cria um gráfico de linha dos dados fornecidos
#plt.plot(x,y)
#essa função exibe o gráfico gerado
#plt.show()

#plt.plot(x,y)
#essa função cria um grafico (plota) com um ponto especifico
#posicao atual na posicao [0], o que seria seu primeiro elemento, é 80
#posicao atual na posicao [1], que seria seu segundo elemento, 80^2
#plt.scatter(posicao_atual[0], posicao_atual[1], color="red")
#plt.show()

taxa_aprendizagem = 0.01

#significa que o codigo vai se repetir 1000x
for _ in range (1000):
   #o novo x vai pegar o primeiro valor (o valor de x) e vai modifica-lo
   #levando-o um pouquinho (taxa de aprendizagem) na direção 
   #contraria da derivada 
   novo_x = posicao_atual[0] - taxa_aprendizagem * derivada_y(posicao_atual[0])
   novo_y = funcao_y(novo_x)
   posicao_atual = (novo_x, novo_y)

   #isso esta dentro do for para que se repita varias vezes
   plt.plot(x,y)
   #adiciona um ponto especifico vermelho do grafico
   plt.scatter(posicao_atual[0], posicao_atual[1], color = "red")
   plt.pause(0.001)
   #remove todos os elementos do gráfico atual, permitindo que um novo 
   #gráfico seja desenhado na próxima iteração do loop
   plt.clf()

print ('oi')
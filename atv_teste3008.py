import numpy as np
import matplotlib.pyplot as plt

def funcao (x, y):
    return ((1 - x)**2) + (100 * (y - (x**2))**2)

def calcular_gradiente(x, y):
   return ((-2) * (1 - x)) - (400 * x * (y - x**2)), 200 * (y - x**2)

x = np.arange (-10, 10, 0.1)
y = np.arange (-6, 6, 0.1)

X, Y = np.meshgrid(x, y)

Z = funcao(X, Y)

pos = (9.8, 0, funcao(9.8, 0))

grade = calcular_gradiente(3, 1)

print (grade)

ax = plt.subplot(projection = "3d")

ax.plot_surface(X, Y, Z, cmap = "viridis")
ax.scatter(pos[0], pos[1], pos[2], color = "red")
plt.show()

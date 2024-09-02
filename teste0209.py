import numpy as np

def rosenbrock_grad(x, y):
    """Calcula o gradiente da função de Rosenbrock."""
    dx = -2 * (1 - x) - 400 * x * (y - x**2)
    dy = 200 * (y - x**2)
    return np.array([dx, dy])

def gradient_descent(alpha, x0, y0, max_iter=10000, tol=1e-6):
    """Executa o gradiente descendente para encontrar o mínimo."""
    x, y = x0, y0
    for _ in range(max_iter):
        grad = rosenbrock_grad(x, y)
        x_new = x - alpha * grad[0]
        y_new = y - alpha * grad[1]

        # Verificar a convergência
        if np.linalg.norm([x_new - x, y_new - y]) < tol:
            break
        
        x, y = x_new, y_new
    
    return x, y

# Parâmetros iniciais
alpha = 0.001
x0, y0 = 0, 0

# Encontrar o mínimo
min_x, min_y = gradient_descent(alpha, x0, y0)
print(f"O mínimo global da função de Rosenbrock é aproximadamente em (x, y) = ({min_x:.4f}, {min_y:.4f})")

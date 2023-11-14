import numpy as np

def tridiagonal_solver(A, B, C, D):
    n = len(B)
    alpha = [0] * n
    beta = [0] * n
    x = [0] * n

    alpha[0] = B[0]
    beta[0] = D[0] / alpha[0]

    for i in range(1, n):
        alpha[i] = B[i] - A[i] * C[i-1] / alpha[i-1]
        beta[i] = (D[i] - A[i] * beta[i-1]) / alpha[i]

    x[n-1] = beta[n-1]

    for i in range(n-2, -1, -1):
        x[i] = beta[i] - C[i] * x[i+1] / alpha[i]

    return x

# Коэффициенты системы
A = [0, 0, 0, -1]  # Диагональ под главной
B = [6, 2, 0.3, 4]  # Главная диагональ
C = [0, 2, 3, 0]  # Диагональ над главной
D = [7, 4.3, 3, -8]  # Столбец правых частей




solutions = tridiagonal_solver(A, B, C, D)
print("Решения:", solutions)



# 

# Задайте коэффициенты вашей системы
A = np.array([[6, 3, 0, 0],
              [1, -2, -0.3, 0],
              [0, 2, 3, -1],
              [0, 0, -1, 4]])

b = np.array([7, 4.3, 3, -8])

# Начальное приближение для решения (можете задать свое)
x0 = np.zeros_like(b)

# Максимальное количество итераций
max_iterations = 1000

# Точность (критерий останова)
tolerance = 1e-6

def jacobi(A, b, x0, max_iterations, tolerance):
    x = x0
    n = len(x)
    for k in range(max_iterations):
        x_new = np.zeros(n)
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        if np.all(np.abs(x - x_new) < tolerance):
            return x_new
        x = x_new
    raise ValueError("Метод Якоби не сошелся после максимального числа итераций.")

# Решение
solution = jacobi(A, b, x0, max_iterations, tolerance)
print("Решение:", solution)

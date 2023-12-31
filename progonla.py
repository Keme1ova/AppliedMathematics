# Размерность матрицы (n x n)
n = 4

# Задание коэффициентов матрицы A и вектора B
A = [[6, 3,	0, 0],
     [1, -2, 0.3,0],
     [0, 2,	3, -1],
     [0, 0, -1, 4]]

B = [7, 4.3, 3, 8]

# Инициализация массивов для хранения результатов
alpha = [0] * n
beta = [0] * n
x = [0] * n

# Прямой ход метода прогонки
alpha[0] = A[0][0]
beta[0] = B[0] / alpha[0]

for i in range(1, n):
    alpha[i] = A[i][i] - A[i][i - 1] * A[i - 1][i] / alpha[i - 1]
    beta[i] = (B[i] - A[i][i - 1] * beta[i - 1]) / alpha[i]

# Обратный ход метода прогонки
x[n - 1] = beta[n - 1]

for i in range(n - 2, -1, -1):
    x[i] = beta[i] - A[i][i + 1] * x[i + 1] / alpha[i]

# Вывод результата
for i in range(n):
    print(f'x{i + 1} = {x[i]}')

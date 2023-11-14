# Размерность матрицы (n x n)
n = 4

# Задание коэффициентов матрицы A и вектора B
A = [[6, 3,	0, 0],
     [1, -2, 0.3,0],
     [0, 2,	3, -1],
     [0, 0, -1, 4]]

B = [7, 4.3, 3, 8]

max_iterations = 100

epsilon = 0.001

x = [0] * n

for iteration in range(max_iterations):
    x_new = [0] * n

    for i in range(n):
        x_new[i] = (B[i] - sum(A[i][j] * x[j] for j in range(n) if j != i)) / A[i][i]

    if all(abs(x_new[i] - x[i]) < epsilon for i in range(n)):
        break

    x = x_new

for i in range(n):
    print(f'x{i + 1} = {x[i]}')

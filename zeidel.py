
n = 4

A = [[6, 3,	0, 0],
     [1, -2, 0.3,0],
     [0, 2,	3, -1],
     [0, 0, -1, 4]]

B = [7, 4.3, 3, 8]

x = [0] * n

max_iterations = 1000


tolerance = 0.001

for iteration in range(max_iterations):
    x_new = x.copy()

    for i in range(n):
        sum1 = sum(A[i][j] * x_new[j] for j in range(i))
        sum2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x_new[i] = (B[i] - sum1 - sum2) / A[i][i]

    error = max(abs(x_new[i] - x[i]) for i in range(n))
    if error < tolerance:
        break

    x = x_new

for i in range(n):
    print(f'x{i + 1} = {x[i]}')

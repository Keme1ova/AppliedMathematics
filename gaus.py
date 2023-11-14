
import numpy as np
# МЕТОДОМ КРАМЕРА
# Матрица коэффициентов
coeff_matrix = np.array([[-4, 4, 7],
                         [2, 0, -5],
                         [-2, -1, 8]])

# Столбец правых частей
constants = np.array([5, 5, -11])


def solve_kramers_rule(coeff_matrix, constants):
    num_variables = len(constants)
    det_coeff = np.linalg.det(coeff_matrix)

    if det_coeff == 0:
        raise ValueError(
            "Матрица коэффициентов сингулярна. Система может не иметь решения или иметь бесконечно много решений.")

    solutions = []

    for i in range(num_variables):
        # Создаем копию матрицы коэффициентов и заменяем i-й столбец столбцом правых частей
        temp_matrix = coeff_matrix.copy()
        temp_matrix[:, i] = constants

        # Вычисляем определитель модифицированной матрицы
        det_temp = np.linalg.det(temp_matrix)

        # Вычисляем решение для i-й переменной
        solution = det_temp / det_coeff
        solutions.append(solution)

    return solutions


solutions = solve_kramers_rule(coeff_matrix, constants)
print("МЕТОДОМ КРАМЕРА:", solutions)




# МЕТОДОМ ГАУССА:
# Матрица коэффициентов
coeff_matrix = np.array([[-4, 4, 7],
                         [2, 0, -5],
                         [-2, -1, 8]])

# Столбец правых частей
constants = np.array([5, 5, -11])


def solve_kramers_rule(coeff_matrix, constants):
    det_coeff = np.linalg.det(coeff_matrix)

    if det_coeff == 0:
        raise ValueError('aa')
            # "Матрица коэффициентов сингулярна. Система может не иметь решения или иметь бесконечно много решений.")

    num_variables = coeff_matrix.shape[1]
    solutions = []

    for i in range(num_variables):
        temp_matrix = coeff_matrix.copy()
        temp_matrix[:, i] = constants
        det_temp = np.linalg.det(temp_matrix)
        solution = det_temp / det_coeff
        solutions.append(solution)

    return solutions


solutions = solve_kramers_rule(coeff_matrix, constants)
print("МЕТОДОМ ГАУССА:", solutions)






# Матрица коэффициентов
coeff_matrix = np.array([[-4, 4, 7],
                         [2, 0, -5],
                         [-2, -1, 8]])

# Столбец правых частей
constants = np.array([5, 5, -11])


def solve_kramers_rule(coeff_matrix, constants):
    det_coeff = np.linalg.det(coeff_matrix)

    if det_coeff == 0:
        raise ValueError('aa')
            # "Матрица коэффициентов сингулярна. Система может не иметь решения или иметь бесконечно много решений.")

    num_variables = coeff_matrix.shape[1]
    solutions = []

    for i in range(num_variables):
        temp_matrix = coeff_matrix.copy()
        temp_matrix[:, i] = constants
        det_temp = np.linalg.det(temp_matrix)
        solution = det_temp / det_coeff
        solutions.append(solution)

    return solutions


solutions = solve_kramers_rule(coeff_matrix, constants)
print("МЕТОДОМ ГАУССА:", solutions)

import numpy as np
from scipy.optimize import linprog

# Коэффициенты целевой функции (расходы на перевозки)
c = [7, 8, 1, 2, 3, 4, 5, 7, 9, 9, 8, 6]

# Матрица коэффициентов для поставок
A_eq = [
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
]

# Вектор правых частей для поставок (запасы в базах)
b_eq = [250, 320, 150]

# Матрица коэффициентов для спроса (поставки в магазины)
A_ub = [
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]
]

# Вектор правых частей для спроса (требуемые поставки в магазинах)
b_ub = [210, 190, 260, 60]

# Границы переменных (неотрицательные поставки)
bounds = [(0, None)] * 12

# Вызов симплекс-метода для минимизации
result = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Вывод результата
print("Оптимальный план перевозок:")
print(np.round(result.x.reshape(3, 4), 2))
print("Минимальные расходы:", result.fun)

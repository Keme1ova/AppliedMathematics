# import numpy as np
#
# def kramer_solver(coefficients_matrix, constants_vector):
#     # Проверяем, является ли матрица квадратной
#     n, m = coefficients_matrix.shape
#     if n != m:
#         raise ValueError("Матрица коэффициентов должна быть квадратной")
#
#     # Проверяем, имеет ли система уравнений единственное решение
#     det_A = np.linalg.det(coefficients_matrix)
#     if abs(det_A) < 1e-6:
#         raise ValueError("Система уравнений не имеет единственного решения")
#
#     # Инициализируем список для хранения корней
#     solution = []
#
#     # Находим корни методом Крамера
#     for i in range(n):
#         # Создаем копию матрицы коэффициентов
#         temp_matrix = coefficients_matrix.copy()
#
#         # Заменяем i-й столбец на вектор констант
#         temp_matrix[:, i] = constants_vector
#
#         # Находим определитель матрицы с замененным столбцом
#         det_temp = np.linalg.det(temp_matrix)
#
#         # Находим корень как отношение определителя с замененным столбцом к определителю исходной матрицы
#         root = det_temp / det_A
#         solution.append(root)
#
#     return solution
#
# # Пример использования
# if __name__ == "__main__":
#     coefficients_matrix = np.array([[-4, 4, 7],
#                                     [2, -5, 0],
#                                     [-2, -1, 8]])
#
#     constants_vector = np.array([5, 5, -11])
#
#     try:
#         roots = kramer_solver(coefficients_matrix, constants_vector)
#         print("Корни СЛАУ:", roots)
#     except ValueError as e:
#         print("Ошибка:", e)


import numpy as np

# Точные значения
x_exact = np.array([1.643, -0.952, 2.511, 2.628])

# Значения для метода Якоби
x_jacobi = np.array([1.643, -0.953, 2.511, 2.627])

# Значения для метода Зейделя
x_seidel = np.array([1.643, -0.952, 2.511, 2.628])

# Вычисление относительной погрешности
relative_error_jacobi = np.linalg.norm(x_jacobi - x_exact) / np.linalg.norm(x_exact)
relative_error_seidel = np.linalg.norm(x_seidel - x_exact) / np.linalg.norm(x_exact)

# Преобразование в проценты
relative_error_jacobi_percent = relative_error_jacobi * 100
relative_error_seidel_percent = relative_error_seidel * 100

print("Относительная погрешность для метода Якоби:", relative_error_jacobi_percent, "%")
print("Относительная погрешность для метода Зейделя:", relative_error_seidel_percent, "%")

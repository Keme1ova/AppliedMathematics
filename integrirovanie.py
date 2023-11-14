# метод левых прямоугольников------------------------------------
def f(x):
    return 3*x**2 - x - 1

def left_rectangles_integration(a, b, n):
    dx = (b - a) / n
    integral = 0.0

    for i in range(n):
        x_i = a + i * dx
        integral += f(x_i) * dx
        print(f"Итерация {i + 1} {integral:.6f}")

    return integral

a = 1  # Начальная точка интегрирования
b = 3  # Конечная точка интегрирования
n = 8  # Количество разбиений

result = left_rectangles_integration(a, b, n)
print(f"Метод левых прямоугольников = {result:.6f}")


# метод средних прямоугольников---------------------------
def f(x):
    return 3 * x**2 - x - 1

def middle_rectangles_integration(a, b, n):
    h = (b - a) / n
    integral = 0.0
    for i in range(n):
        x_i = a + (i + 0.5) * h
        integral += f(x_i) * h
        print(f"Итерация {i+1}: {integral}")
    return integral

a = 1  # Начало интервала
b = 3  # Конец интервала
n = 8  # Количество подинтервалов

result = middle_rectangles_integration(a, b, n)
print(f"Метод средних прямоугольников: {result}")


# метод трапеции------------------------------------
def trapezoidal_integration(f, a, b, n):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    integral *= h
    return integral

# Функция, которую вы хотите интегрировать
def func(x):
    return 3 * x**2 - x - 1

# Граничные точки и количество интервалов
a = 1
b = 3
n = 8

# Вызов функции интегрирования
result = trapezoidal_integration(func, a, b, n)

print("Метод трапеции:", result)



# метод Симпсона------------------------------------

def f(x):
    return 3 * x**2 - x - 1

def simpsons_rule(a, b, n):
    h = (b - a) / n
    integral = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)

        print(f"Итерация {i} = {integral * (h / 3)}")

    return integral * (h / 3)

a = 1
b = 3
n = 8

result = simpsons_rule(a, b, n)
print(f"Метод Симпсона = {result}")

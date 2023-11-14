# полином Лагранжа
def lagrange_polynomial(x, y):
    """
    Строит полином Лагранжа на основе узлов интерполяции (x, y).

    :param x: список значений x (узлы интерполяции)
    :param y: список значений y (значения функции в узлах интерполяции)
    :return: Строка с полиномом Лагранжа
    """
    # if len(x) != len(y):
    #     raise ValueError("Списки x и y должны иметь одинаковую длину")

    n = len(x)
    result = ""

    for i in range(n):
        term = f"{y[i]:+.2f}"  # Форматирование значения y с знаком
        for j in range(n):
            if i != j:
                term += f" * (x - {x[j]}) / ({x[i]} - {x[j]})"
        if i == 0:
            result += term
        else:
            result += " + " + term

    return result

# Пример использования:
x = [2, 3, 4]
y = [1, 0, 2]

lagrange_poly = lagrange_polynomial(x, y)
print(f"Полином Лагранжа: P(x) = {lagrange_poly}")

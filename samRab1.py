import math

#Метод деления отрезка пополам
# def f(x):
#     return math.exp(x/2) - x - 3

# a = -2.75
# b = 3.8
# e = 0.001
# iteration = 0

# while abs(b-a) > e:
#     c = (a+b)/2
#     if f(c) == 0:
#         break
#     elif f(a)*f(c) < 0:
#         b = c
#     else:
#         a = c
#     iteration += 1
#     print(f"{iteration}: a = {a}, b = {b}, x = {c}, b-a = {b-a}")

# print(f"Метод деления отрезка пополам {c}")




# МЕТОД НЬЮТОНА
def f(x):
    return math.exp(x/2) - x - 3

def df(x):
    return 0.5 * math.exp(x/2) - 1

def newton_method(x0, tol, max_iter):
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        x1 = x0 - fx / dfx
        print( i+1, ": x =", x1, f"E: " ,x0-x1)
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    print("Maximum iterations exceeded.")
    return None

# Пример использования
x0 = 1.0
tol = 1e-6
max_iter = 100
root = newton_method(x0, tol, max_iter)
print("МЕТОД НЬЮТОНА:", root)

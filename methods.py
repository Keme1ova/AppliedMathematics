import math

# МЕТОД ПРОСТЫХ ИТЕРАЦИЙ
def f(x):
    return math.exp(x/2) - x - 3

def g(x):
    return math.exp(x/2) - 3

def simple_iteration_method(x0, eps):
    i = 0
    while True:
        x1 = g(x0)
        fx1 = f(x1)
        print( i+1, ": x =", x1, ", f(x) =", fx1 ,f"E = {x0-x1} ")
        if abs(x1-x0) < eps:
            break
        x0 = x1
        i += 1
    return x1

x0 = 0
eps = 0.001
root = simple_iteration_method(x0, eps)
print("МЕТОД ПРОСТЫХ ИТЕРАЦИЙ:", root)




# МЕТОД ХОРД
def f(x):
    return math.exp(x/2) - x - 3


def chord_method(x0, a, b, e):
    iteration = 1
    while True:
        fx0 = f(x0)
        x1 = x0 - (fx0 * (b - x0)) / (f(b) - fx0)
        fx1 = f(x1)

        print(f" {iteration}: x0 = {x0:.6f}, f(x0) = {fx0:.6f} E = {x0-x1} ")

        if abs(fx1) < e:
            print(f"МЕТОД ХОРД: x = {x1:.6f}, f(x) = {fx1:.6f} , E = {x0-x1} ")
            break

        x0 = x1
        iteration += 1


x0 = 0.55
a = 0
b = 1
e = 0.001

chord_method(x0, a, b, e)




# МЕТОД СЕКУЩИХ
def f(x):
    return math.exp(x/2) - x - 3

def secant_method(x0, a, e):
    iteration = 1
    x1 = x0 + a
    while abs(f(x1)) > e:
        fx0 = f(x0)
        fx1 = f(x1)
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        print(f" {iteration}: x0 = {x0}, x1 = {x1}, x2 = {x2}, F(x2) = {fx1}, E = {x0-x1} ")
        x0 = x1
        x1 = x2
        iteration += 1
    return x2

x0 = 0.55
a = 0.1
e = 0.001

root = secant_method(x0, a, e)
print(f"МЕТОД СЕКУЩИХ: {root} ")



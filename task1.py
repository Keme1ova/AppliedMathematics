# # #Метод деления отрезка пополам
# def f(x):
#     return x**3 + x - 1

# a = 0
# b = 1
# e = 0.001

# while b - a > e:
#     c = (a + b) / 2
#     if f(c) == 0:
#         break
#     elif f(a) * f(c) < 0:
#         b = c
#     else:
#         a = c
# print("Метод деления отрезка пополам:", c)


# #Метод Ньютона (метод касательных)
# def f(x):
#     return x**3 + x - 1

# def df(x):
#     return 3*x**2 + 1

# x0 = 0.5
# e = 0.001

# while True:
#     xn = x0 - f(x0) / df(x0)
#     if abs(xn - x0) < e:
#         break
#     x0 = xn

# print("Метод Ньютона:", xn)



#Метод деления отрезка пополам
def f(x):
    return x**3 + x - 1

a = 0
b = 1
epsilon = 0.001
iteration = 0

while abs(b-a) > epsilon:
    e = b-a
    c = (a+b)/2
    iteration += 1
    if f(a)*f(c) < 0:
        b = c
    else:
        a = c
    print(f"{iteration}: a = {a}, b = {b}, c = {c} e = {e} ")

print(f"Метод деления отрезка пополам:{c}")


#Метод Ньютона (метод касательных)

def f(x):
    return x**3 + x - 1

def f_prime(x):
    return 3*x**2 + 1

x0 = 0.5
epsilon = 0.001
iteration = 0

while abs(f(x0)/f_prime(x0)) > epsilon:
    x1 = x0 - f(x0)/f_prime(x0)
    iteration += 1
    print(f"{iteration}: x0 = {x0}, x1 = {x1}")
    x0 = x1

print(f"Метод Ньютона:{x1}")
def less_squares(y: list[float], x: list[float]) -> tuple[float, float] or None:
    if len(y) != len(x):
        return

    n: int = len(x)
    a: float
    b: float

    xy_sum: float = 0

    x_sum: float = 0
    y_sum: float = 0
    x_sq_sum: float = 0

    for i in range(n):
        xy_sum += x[i] * y[i]
        x_sum += x[i]
        y_sum += y[i]
        x_sq_sum += x[i] ** 2

    sq_sum_x: float = x_sum ** 2

    a_numerator: float = n * xy_sum - x_sum * y_sum
    b_numerator: float = x_sq_sum * y_sum - x_sum * xy_sum
    denominator: float = n * x_sq_sum - sq_sum_x

    a = a_numerator / denominator
    b = b_numerator / denominator

    return (a, b)

#task_5
x: list[float] = [4.25, 4.3, 4.4, 4.42, 4.45, 4.5 ,4.53, 4.55, 4.6, 4.62]
y: list[float] = [530, 540, 553, 554, 557, 560, 565, 568, 571, 572]

k, b = less_squares(y, x)

volume = 3.0
costs = k * volume + b

print(f"{k = }, {b = }")
# print( f'y =' + {k} + '*a' +  {b})
# print(f"Затраты на производстве при {volume} у.е равняются {costs} рублям")
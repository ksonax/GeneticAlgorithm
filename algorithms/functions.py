def beale_function(x):
    y = pow((1.5 - x[0] + x[0] * x[1]), 2) + pow(2.25 - x[0] + x[0] * pow(x[1], 2), 2) + pow(
        (2.625 - x[0] + x[0] * pow(x[1], 3)), 2)
    return y


# 2
def beale_function_plot(x1, x2):
    y = pow((1.5 - x1 + x1 * x2), 2) + pow(2.25 - x1 + x1 * pow(x2, 2), 2) + pow((2.625 - x1 + x1 * pow(x2, 3)), 2)
    return y

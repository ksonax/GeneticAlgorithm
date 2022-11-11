from math import pi, sin, cos, sqrt, fabs, exp


# 1
def acklay_function():
    return 0


# 2
def beale_function(x1, x2):
    return pow((1.5 - x1 + x1 * x2), 2) + pow(2.25 - x1 + x1 * pow(x2, 2), 2) + pow((2.625 - x1 + x1 * pow(x2, 3)), 2)


# 3
def branin_function(x1, x2, a=1, b=5.1 / (4 * pow(pi, 2)), c=5 / pi, r=6, s=10, t=1 / (8 * pi)):
    return a * pow((x2 - b * pow(x1, 2) + c * x1 - r), 2) + s * (1 - t) * cos(x1) + s


# 4
def bohachevsky_function():
    return 0


# 5
def booth_function(x1, x2):
    return pow(x1 + 2 * x2 - 7, 2) + pow(2 * x1 + x2 - 5, 2)


# 6
def bukin_function(x1, x2):
    return 100 * sqrt(fabs(x2 - 0.01 * pow(x1, 2))) + 0.01 * fabs(x1 + 10)


# 7
def cross_in_tray_function(x1, x2):
    return -0.0001 * pow(fabs(sin(x1) * sin(x2) * exp(fabs(100 - sqrt(pow(x1, 2) + pow(x2, 2) / pi)))) + 1, 0.1)


# 8
def drop_wave_function(x1, x2):
    return -1 * (1 + cos(12 * sqrt(pow(x1, 2) + pow(x2, 2)))) / (0.5 * (pow(x1, 2) + pow(x2, 2)) + 2)


# 9
def eggholder_function(x1, x2):
    return -1 * (x2 + 47) * sin(sqrt(fabs(x2 + x1 / 2 + 47))) - x1 * sin(sqrt(fabs(x1 - (x2 + 47))))


# 10
def easom_function(x1, x2):
    return -1 * cos(x1) * cos(x2) * exp(-1 * pow((x1 - pi), 2) - pow((x2 - pi), 2))

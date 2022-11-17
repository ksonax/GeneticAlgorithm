from numpy.random import randint
from numpy.random import rand


def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y


# Cross 1 punkt
def crossover(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
        pt = randint(1, len(p1) - 2)
        # perform crossover
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]


# Cross 2 punkt
def crossover2(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
        pt1 = randint(1, (len(p1) - 2) / 2)
        pt2 = randint((len(p1) - 2) / 2, len(p1) - 2)
        # perform crossover
        c1 = p1[:pt1] + p2[pt1:pt2] + p1[pt2:]
        c2 = p2[:pt1] + p1[pt1:pt2] + p2[pt2:]
    return [c1, c2]


# Cross 3 punkt
def crossover3(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
        pt1 = randint(1, (len(p1) - 2) / 3)
        pt2 = randint((len(p1) - 2) / 3, 2 * (len(p1) - 2) / 3)
        pt3 = randint(2 * (len(p1) - 2) / 3, len(p1) - 2)
        # perform crossover
        c1 = p1[:pt1] + p2[pt1:pt2] + p1[pt2:pt3] + p2[pt3:]
        c2 = p2[:pt1] + p1[pt1:pt2] + p2[pt2:pt3] + p1[pt3:]
    return [c1, c2]


def uniformCrossover(p1, p2):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    for i in range(1, len(c1)):
        if rand() <= 0.50:
            c1[i], c2[i] = swap(c1[i], c2[i])
    return [c1, c2]



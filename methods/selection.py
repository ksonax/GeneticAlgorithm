# genetic algorithm search for continuous function optimization
from numpy.random import randint
import random


def tournament(pop, scores, k):
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k - 1):
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]


def best(pop, scores, k):
    p = []
    for i in range(0, len(pop)):
        p.append([scores[i], pop[i]])
    p.sort()
    p.reverse()
    d2 = [item[1] for item in p]
    return d2[k]


def roulette(pop, scores):
    suma = 0
    for i in range(0, len(scores)):
        suma += scores[i]
    p = []
    temp = 0
    for i in range(0, len(pop)):
        p.append(scores[i] / suma)
    r = random.uniform(0, 1)
    for i in range(0, len(pop)):
        temp += p[i]
        if temp > r:
            x = i
            break
    return pop[x]

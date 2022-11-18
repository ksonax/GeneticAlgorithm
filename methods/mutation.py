from numpy.random import rand


def edge_mutation(bitstring, r_mut):
    for i in range(len(bitstring)):
        if rand() < r_mut:
            bitstring[i] = 1 - bitstring[i]
    return bitstring


def op_mutation(bitstring, r_mut):
    for i in range(1, len(bitstring) - 1):
        if rand() < r_mut:
            bitstring[i] = 1 - bitstring[i]
            break
    return bitstring


def tp_mutation(bitstring, r_mut):
    j = 0
    for i in range(1, len(bitstring) - 1):
        if rand() < r_mut:
            bitstring[i] = 1 - bitstring[i]
            j += 1
        if j == 2:
            break
    return bitstring

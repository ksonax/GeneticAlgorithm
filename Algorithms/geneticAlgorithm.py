# genetic algorithm search for continuous function optimization
from numpy.random import randint
from numpy.random import rand
from Algorithms.Function import beale_function
import Methods.mutation as mutation
import Methods.cross as cross
import Methods.selection as select

def inversion(bitstring:list, r_inve):
    c1 = bitstring.copy()
    # check for recombination
    if rand() < r_inve:
        # select crossover point that is not on the end of the string
        pt1 = randint(1, (len(bitstring) - 2) / 2)
        pt2 = randint((len(bitstring) - 2) / 2, len(bitstring) - 2)
        # perform crossover
        x =bitstring[pt1:pt2]
        x.reverse()
        c1 = bitstring[:pt1] + x + bitstring[pt2:]
    return c1



# decode bitstring to numbers
def decode(bounds, n_bits, bitstring):
    decoded = list()
    largest = 2 ** n_bits
    for i in range(len(bounds)):
        # extract the substring
        start, end = i * n_bits, (i * n_bits) + n_bits
        substring = bitstring[start:end]
        # convert bitstring to a string of chars
        chars = ''.join([str(s) for s in substring])
        # convert string to integer
        integer = int(chars, 2)
        # scale integer to desired range
        value = bounds[i][0] + (integer / largest) * (bounds[i][1] - bounds[i][0])
        # store
        decoded.append(value)
    return decoded


# genetic algorithm
def genetic_algorithm( bounds, n_bits, n_iter, n_pop, r_cross, r_mut, r_inve):
    # initial population of random bitstring
    pop = [randint(0, 2, n_bits * len(bounds)).tolist() for _ in range(n_pop)]
    # keep track of best solution
    best, best_eval = 0, beale_function(decode(bounds, n_bits, pop[0]))
    # enumerate generations
    thebest = []

    for gen in range(n_iter):

        # decode population
        decoded = [decode(bounds, n_bits, p) for p in pop]
        # evaluate all candidates in the population
        scores = [beale_function(d) for d in decoded]
        # check for new best solution
        for i in range(n_pop):
            #TUTAJ ZMIENIC jak COS
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
                print(">%d, new best f(%s) = %f" % (gen, decoded[i], scores[i]))
        # select parents
        selected = [select.best(pop, scores, _) for _ in range(n_pop)]
        # create the next generation
        children = list()
        children.append(best)
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i + 1]
            # crossover and mutation
            for c in cross.crossover(p1, p2, r_cross):
                # mutation
                c = mutation.tp_mutation(c, r_mut)
                c = inversion(c,r_inve)
                # store for next generation
                children.append(c)
        # replace population
        pop = children
    return [best, best_eval]


# define range for input
bounds = [[-4.5, 4.5], [-4.5, 4.5]]
# define the total iterations
n_iter = 1000
# bits per variable
n_bits = 16
# define the population size
n_pop = 100
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 0.50
# best amount
r_best = 3
# inversion rate
r_inve = 0.3
#1.0 / (float(n_bits) * len(bounds))
# perform the genetic algorithm search
best, score = genetic_algorithm(bounds, n_bits, n_iter, n_pop, r_cross, r_mut, r_inve)
print('Done!')
decoded = decode(bounds, n_bits, best)
print('f(%s) = %f' % (decoded, score))




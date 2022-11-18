# genetic algorithm search for continuous function optimization
from numpy.random import randint
from numpy.random import rand
from algorithms.functions import beale_function
import methods.mutation as mutation
import methods.cross as cross
import methods.selection as select
from ui.UserInputs import UserInputs
from statistics import stdev, mean


def inversion(bitstring: list, r_inve):
    c1 = bitstring.copy()
    if rand() < r_inve:
        pt1 = randint(1, (len(bitstring) - 2) / 2)
        pt2 = randint((len(bitstring) - 2) / 2, len(bitstring) - 2)
        x = bitstring[pt1:pt2]
        x.reverse()
        c1 = bitstring[:pt1] + x + bitstring[pt2:]
    return c1


# decode bitstring to numbers
def decode(bounds, n_bits, bitstring):
    decoded = list()
    largest = 2 ** n_bits
    for i in range(len(bounds)):
        start, end = i * n_bits, (i * n_bits) + n_bits
        substring = bitstring[start:end]
        chars = ''.join([str(s) for s in substring])
        integer = int(chars, 2)
        value = bounds[i][0] + (integer / largest) * (bounds[i][1] - bounds[i][0])
        decoded.append(value)
    return decoded


def genetic_algorithm(user_input):
    bounds = [[user_input.begin_range_a, user_input.end_range_b], [user_input.begin_range_a, user_input.end_range_b]]
    pop = [randint(0, 2, user_input.number_of_bits * len(bounds)).tolist() for _ in range(user_input.population_amount)]
    best, best_eval = 0, beale_function(decode(bounds, user_input.number_of_bits, pop[0]))
    gen_b_rows = []
    gen_avg_rows = []
    gen_std_dev_rows = []
    for gen in range(user_input.epochs_amount):
        decoded = [decode(bounds, user_input.number_of_bits, p) for p in pop]
        scores = [beale_function(d) for d in decoded]
        best_iter = scores[0]
        for i in range(user_input.population_amount):
            if user_input.maximum:
                if scores[i] > best_eval:
                    best, best_eval = pop[i], scores[i]
                    print(">%d, new best f(%s) = %f" % (gen, decoded[i], scores[i]))
                if scores[i] > best_iter:
                    best_iter = scores[i]
            else:
                if scores[i] < best_eval:
                    best, best_eval = pop[i], scores[i]
                    print(">%d, new best f(%s) = %f" % (gen, decoded[i], scores[i]))
                if scores[i] < best_iter:
                    best_iter = scores[i]
        gen_b_rows.append([str(gen), str(best_iter)])
        gen_avg_rows.append([str(gen), mean(scores)])
        gen_std_dev_rows.append([str(gen), str(stdev(scores))])
        if user_input.selection_method == "Tournament":
            selected = [select.tournament(pop, scores, user_input.best_and_tournament_chromosome_amount) for _ in
                        range(user_input.population_amount)]
        if user_input.selection_method == "Roulette":
            selected = [select.roulette(pop, scores) for _ in range(user_input.population_amount)]
        if user_input.selection_method == "Best":
            selected = [select.best(pop, scores, _) for _ in range(user_input.population_amount)]
        children = list()
        if user_input.elite_strategy:
            children.append(best)
        for i in range(0, user_input.population_amount, 2):
            p1, p2 = selected[i], selected[i + 1]
            if user_input.cross_method == "One Point Cross":
                cross_result = cross.crossover(p1, p2, user_input.cross_probability)
            if user_input.cross_method == "Two Point Cross":
                cross_result = cross.crossover2(p1, p2, user_input.cross_probability)
            if user_input.cross_method == "Three Point Cross":
                cross_result = cross.crossover3(p1, p2, user_input.cross_probability)
            if user_input.cross_method == "Uniform Cross":
                cross_result = cross.uniformCrossover(p1, p2)
            for c in cross_result:
                if user_input.mutation_method == "Edge":
                    c = mutation.edge_mutation(c, user_input.mutation_probability)
                if user_input.mutation_method == "One Point":
                    c = mutation.op_mutation(c, user_input.mutation_probability)
                if user_input.mutation_method == "Two Point":
                    c = mutation.tp_mutation(c, user_input.mutation_probability)
                c = inversion(c, user_input.inversion_probability)
                children.append(c)
        pop = children

    print('Done!')
    decoded = decode(bounds, user_input.number_of_bits, best)
    print('f(%s) = %f' % (decoded, best_eval))
    return [decoded, best_eval, gen_b_rows, gen_avg_rows, gen_std_dev_rows]


defaultUser = UserInputs(
    begin_range_a=-4.5,
    end_range_b=4.5,
    population_amount=100,
    number_of_bits=16,
    epochs_amount=1000,
    best_and_tournament_chromosome_amount=3,
    cross_probability=0.5,
    mutation_probability=0.1,
    inversion_probability=0.1,
    selection_method="Best",
    cross_method="cross",
    mutation_method="mutate",
    maximum=False,
    elite_strategy=True,
)

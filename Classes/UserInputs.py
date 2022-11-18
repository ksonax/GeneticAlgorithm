class UserInputs:

    def __init__(
            self,
            begin_range_a,
            end_range_b,
            population_amount,
            number_of_bits,
            epochs_amount,
            best_and_tournament_chromosome_amount,
            cross_probability,
            mutation_probability,
            inversion_probability,
            selection_method,
            cross_method,
            mutation_method,
            maximum,
            elite_strategy,

    ):
        self.begin_range_a = begin_range_a
        self.end_range_b = end_range_b
        self.population_amount = population_amount
        self.number_of_bits = number_of_bits
        self.epochs_amount = epochs_amount
        self.best_and_tournament_chromosome_amount = best_and_tournament_chromosome_amount
        self.cross_probability = cross_probability
        self.mutation_probability = mutation_probability
        self.inversion_probability = inversion_probability
        self.selection_method = selection_method
        self.cross_method = cross_method
        self.mutation_method = mutation_method
        self.maximum = maximum
        self.elite_strategy = elite_strategy

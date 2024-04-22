import random
POPULATION_SIZE = 6
CHROMOSOME_LENGTH = 5
MUTATION_RATE = 0.1
population = [
    [0, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1]
]
def binary_to_decimal(binary_chromosome):
    decimal_value = 0
    for bit in binary_chromosome:
        decimal_value = (decimal_value << 1) | bit
    return decimal_value
def calculate_fitness(binary_chromosome):
    x = binary_to_decimal(binary_chromosome)
    fitness_value = x ** 2 + 3 * x + 5
    return fitness_value
def mutate(chromosome):
    mutated_chromosome = []
    for bit in chromosome:
        if random.random() < MUTATION_RATE:
            mutated_bit = 1 - bit
        else:
            mutated_bit = bit
        mutated_chromosome.append(mutated_bit)
    return mutated_chromosome
def main():
    mutated_population = []
    for chromosome in population:
        mutated_chromosomes = mutate(chromosome)
        mutated_population.append(mutated_chromosomes)
    print("Child after crossover:")
    for i, chromosome in enumerate(population):
        x_value = binary_to_decimal(chromosome)
        print(f"Chromosome {i+1}: {chromosome} -> X value (decimal value): {x_value}")
    fitness_values = []
    print("\nChild after flipping (mutated population):")
    for i, chromosome in enumerate(mutated_population):
        x_value = binary_to_decimal(chromosome)
        fitness_value = calculate_fitness(chromosome)
        fitness_values.append(fitness_value)
        print(f"Chromosome {i+1}: {chromosome} -> X value: {x_value} -> Fitness Value: {fitness_value}")
    print("\nFitness Statistics:")
    total_fitness = sum(fitness_values)
    avg_fitness = total_fitness / len(population)
    max_fitness = max(fitness_values)
    print(f"Sum of the fitness values: {total_fitness}")
    print(f"Average of the fitness values: {avg_fitness}")
    print(f"Maximum fitness value: {max_fitness}")
if __name__=="__main__":
    main()
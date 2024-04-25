import random
POPULATION_SIZE = 6
CHROMOSOME_LENGTH = 5  # Length of each chromosome in bits (for binary representation)
MUTATION_RATE = 0.1  # Mutation rate (10%)
# Define your initial binary-encoded chromosomes
population = [
    [0, 1, 1, 0, 0],  # chromosome 1
    [0, 1, 0, 0, 1],  # chromosome 2
    [1, 1, 0, 0, 1],  # chromosome 3
    [1, 0, 0, 1, 1],  # chromosome 4
    [0, 0, 1, 1, 1],  # chromosome 5
    [0, 1, 1, 0, 0]   # chromosome 6
]
def binary_to_decimal(binary_chromosome):
    # Convert binary chromosome to a decimal integer
    decimal_value = 0
    for bit in binary_chromosome:
        decimal_value = (decimal_value << 1) | bit
    return decimal_value
def calculate_fitness(binary_chromosome):
    # Decode binary chromosome to obtain the value of x
    x = binary_to_decimal(binary_chromosome)
    # Calculate the fitness based on the equation y = x^2 + 3x + 5
    fitness_value = x ** 2 + 3 * x + 5
    return fitness_value
def mutate(chromosome):
    # Perform mutation on a chromosome with a given mutation rate
    mutated_chromosome = []
    for bit in chromosome:
        if random.random() < MUTATION_RATE:
            # Flip the bit (mutate)
            mutated_bit = 1 - bit
        else:
            mutated_bit = bit
        mutated_chromosome.append(mutated_bit)
    return mutated_chromosome
def main():
    # Perform one iteration of mutation on the population
    mutated_population = []
    for chromosome in population:
        mutated_chromosome = mutate(chromosome)
        mutated_population.append(mutated_chromosome)
    # Display mutated population and calculate fitness
    print("Child after crossover:")
    for i, chromosome in enumerate(population):
        x_value = binary_to_decimal(chromosome)
        print(f"Chromosome {i + 1}: {chromosome} -> X value: {x_value}")
    print("\nChild after flipping (Mutated Population):")
    fitness_values = []
    for i, chromosome in enumerate(mutated_population):
        x_value = binary_to_decimal(chromosome)
        fitness = calculate_fitness(chromosome)
        fitness_values.append(fitness)
        print(f"Chromosome {i + 1}: {chromosome} -> X value: {x_value} -> Fitness value: {fitness}")
    # Calculate fitness statistics
    total_fitness = sum(fitness_values)
    average_fitness = total_fitness / len(population)
    max_fitness = max(fitness_values)
    print("\nFitness Statistics:")
    print(f"Sum of Fitness Values: {total_fitness}")
    print(f"Average of Fitness Values: {average_fitness}")
    print(f"Maximum Fitness Value: {max_fitness}")
if __name__ == "__main__":
    main()

import random

POPULATION_SIZE = 6
CHROMOSOME_LENGTH = 8  # Length of each chromosome in bits (for binary representation)
MUTATION_RATE = 0.1  # Mutation rate (10%)

def create_population():
    # Create a population of random binary-encoded chromosomes
    population = []
    for _ in range(POPULATION_SIZE):
        chromosome = [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]
        population.append(chromosome)
    return population

def binary_to_decimal(binary_chromosome):
    # Convert binary chromosome to a decimal integer
    decimal_value = 0
    for bit in binary_chromosome:
        decimal_value = (decimal_value << 1) | bit
    return decimal_value

def mutate(chromosome):
    # Perform mutation on a chromosome by flipping random bits based on the mutation rate
    mutated_chromosome = chromosome[:]
    for i in range(len(mutated_chromosome)):
        if random.random() < MUTATION_RATE:
            mutated_chromosome[i] = 1 - mutated_chromosome[i]  # Flip the bit (0 to 1 or 1 to 0)
    return mutated_chromosome

def main():
    # Create initial population
    population = create_population()

    # Perform one iteration of mutation
    new_population = []

    for chromosome in population:
        mutated_chromosome = mutate(chromosome)
        new_population.append(mutated_chromosome)

    # Display results
    print("Initial Population:")
    for i, chromosome in enumerate(population):
        print(f"Chromosome {i + 1}: {chromosome} -> Decimal value: {binary_to_decimal(chromosome)}")

    print("\nAfter Mutation (One Iteration):")
    for i, chromosome in enumerate(new_population):
        print(f"Chromosome {i + 1}: {chromosome} -> Decimal value: {binary_to_decimal(chromosome)}")

if __name__ == "__main__":
    main()

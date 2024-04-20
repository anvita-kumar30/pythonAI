import random

POPULATION_SIZE = 6
CHROMOSOME_LENGTH = 8  # Length of each chromosome in bits (for binary representation)
CROSSOVER_RATE = 0.25  # Crossover rate (25%)

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

def crossover(parent1, parent2):
    # Perform single-point crossover between two parent chromosomes
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, CHROMOSOME_LENGTH - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
    else:
        child1 = parent1
        child2 = parent2
    return child1, child2

def main():
    # Create initial population
    population = create_population()

    # Perform one iteration of crossover
    random.shuffle(population)  # Shuffle population for random pairing
    new_population = []

    for i in range(0, len(population), 2):
        if i + 1 < len(population):
            parent1 = population[i]
            parent2 = population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(child1)
            new_population.append(child2)
        else:
            # If the population size is odd, keep the last chromosome unchanged
            new_population.append(population[i])

    # Display results
    print("Initial Population:")
    for i, chromosome in enumerate(population):
        print(f"Chromosome {i + 1}: {chromosome} -> Decimal value: {binary_to_decimal(chromosome)}")

    print("\nAfter Crossover (One Iteration):")
    for i, chromosome in enumerate(new_population):
        print(f"Chromosome {i + 1}: {chromosome} -> Decimal value: {binary_to_decimal(chromosome)}")

if __name__ == "__main__":
    main()

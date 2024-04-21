import random
POPULATION_SIZE = 6
CHROMOSOME_LENGTH = 5  # Length of each chromosome in bits (for binary representation)
CROSSOVER_RATE = 0.25  # Crossover rate (25%)
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
    # Perform one iteration of crossover
    new_population = []
    for i in range(0, len(population), 2):
        if i + 1 < len(population):
            parent1 = population[i]
            parent2 = population[i + 1]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(child1)
            new_population.append(child2)
    print("Initial Population:")
    for i, chromosome in enumerate(population):
        x_value = binary_to_decimal(chromosome)
        print(f"Chromosome {i + 1}: {chromosome} -> Crossover point (decimal value): {x_value}")
    print("\nChild After Crossover (One Iteration):")
    fitness_values = []
    for i, chromosome in enumerate(new_population):
        fitness = calculate_fitness(chromosome)
        fitness_values.append(fitness)
        x_value = binary_to_decimal(chromosome)
        print(f"Chromosome {i + 1}: {chromosome} -> X value: {x_value} -> Fitness value: {fitness}")
    total_fitness = sum(fitness_values)
    average_fitness = total_fitness / len(population)
    max_fitness = max(fitness_values)
    print("\nFitness Statistics:")
    print(f"Sum of Fitness Values: {total_fitness}")
    print(f"Average of Fitness Values: {average_fitness}")
    print(f"Maximum Fitness Value: {max_fitness}")

if __name__ == "__main__":
    main()

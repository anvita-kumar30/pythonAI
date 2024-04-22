import random
POPULATION_SIZE = 6
CHROMOSOME_LENGTH = 5
CROSSOVER_RATE = 0.25
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
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, CHROMOSOME_LENGTH-1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
    else:
        child1 = parent1
        child2 = parent2
    return child1, child2
def main():
    new_population = []
    for i in range(0, len(population), 2):
        parent1 = population[i]
        parent2 = population[i+1]
        child1,  child2 = crossover(parent1, parent2)
        new_population.append(child1)
        new_population.append(child2)
    print("Initial Population:")
    for i, chromosome in enumerate(population):
        x_value = binary_to_decimal(chromosome)
        print(f"Chromosome {i+1}: {chromosome} -> Crossover point (decimal value): {x_value}")
    fitness_values = []
    print("\nChild after crossover (one iteration):")
    for i, chromosome in enumerate(new_population):
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
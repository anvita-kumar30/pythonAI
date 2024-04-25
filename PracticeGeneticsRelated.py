# Genetics
# import random
# POPULATION_SIZE = 6
# GENES = [str(i) for i in range(10)]
# TARGET = 30
# MAX_ITERATIONS = 50
# class Chromosome:
#     def __init__(self, genes):
#         self.genes = genes
#         self.fitness = self.calculate_fitness()
#     def calculate_fitness(self):
#         a, b, c, d = [int(gene) for gene in self.genes]
#         return abs((a + 2*b + 3*c + 4*d) - TARGET)
#     def crossover(self, other):
#         crossover_point = random.randint(1, len(self.genes) - 1)
#         child_genes = (
#             self.genes[:crossover_point] +
#             other.genes[crossover_point:]
#         )
#         return Chromosome(child_genes)
#     def mutate(self):
#         mutated_gene_indices = random.sample(range(len(self.genes)), random.randint(1,2))
#         mutated_genes = [
#             random.choice(GENES) if idx in mutated_gene_indices else gene
#             for idx, gene in enumerate(self.genes)
#         ]
#         return Chromosome(mutated_genes)
# def selection(population):
#     sorted_population = sorted(population, key=lambda x: x.fitness)
#     return sorted_population[:2]
# def main():
#     population = [
#         Chromosome(['10', '12', '22', '43']),
#         Chromosome(['2', '54', '11', '22']),
#         Chromosome(['14', '8', '9', '12']),
#         Chromosome(['9', '4', '32', '32']),
#         Chromosome(['32', '12', '1', '21']),
#         Chromosome(['4', '98', '9', '6'])
#     ]
#     print("Initial Chromosomes: ")
#     for i, chromosome in enumerate(population, 1):
#         print(f"Chromosome {i}: {chromosome.genes}")
#     iteration = 0
#     best_solution = None
#     while iteration < MAX_ITERATIONS:
#         parent1, parent2 = selection(population)
#         child = parent1.crossover(parent2)
#         child = child.mutate()
#         population.remove(max(population, key=lambda x: x.fitness))
#         population.append(child)
#         best_chromosome = min(population, key=lambda x: x.fitness)
#         if best_solution is None or best_chromosome.fitness < best_solution.fitness:
#             best_solution = best_chromosome
#         iteration += 1
#     print("\nFinal Chromosomes: ")
#     for i, chromosome in enumerate(population, 1):
#         print(f"Chromosome {i}: {chromosome.genes}")
#     print(f"\nBest Chromosome: {best_solution.genes}")
#     print(f"Best Solution: {sum((i+1)*int(gene) for i, gene in enumerate(best_solution.genes))}")
#     print(f"Values of a, b, c, d: {tuple(int(gene) for gene in best_solution.genes)}")
#     print(f"Number of iterations: {iteration}")
# if __name__ == "__main__":
#     main()

# Crossover
# import random
# POPULATION_SIZE = 6
# CHROMOSOME_LENGTH = 5
# CROSSOVER_RATE = 0.25
# population = [
#     [0, 1, 1, 0, 1],
#     [0, 1, 1, 0, 1],
#     [0, 1, 1, 0, 1],
#     [0, 1, 1, 1, 1],
#     [0, 1, 0, 1, 1],
#     [1, 1, 0, 0, 1],
# ]
# def binary_to_decimal(binary_chromosome):
#     decimal_value = 0
#     for bit in binary_chromosome:
#         decimal_value = (decimal_value << 1) | bit
#     return decimal_value
# def calculate_fitness(binary_chromosome):
#     x = binary_to_decimal(binary_chromosome)
#     fitness_value = x**2 + 3*x + 5
#     return fitness_value
# def crossover(parent1, parent2):
#     if random.random() < CROSSOVER_RATE:
#         crossover_point = random.randint(1, CHROMOSOME_LENGTH-1)
#         child1 = parent1[:crossover_point] + parent2[crossover_point:]
#         child2 = parent2[:crossover_point] + parent1[crossover_point:]
#     else:
#         child1 = parent1
#         child2 = parent2
#     return child1, child2
#
# def main():
#     new_population = []
#     for i in range(0, len(population), 2):
#         if i + 1 < len(population):
#             parent1 = population[i]
#             parent2 = population[i+1]
#             child1, child2 = crossover(parent1, parent2)
#             new_population.append(child1)
#             new_population.append(child2)
#     print("Initial population:")
#     for i, chromosome in enumerate(population):
#         x_value = binary_to_decimal(chromosome)
#         print(f"Chromosome {i+1}: {chromosome} -> Crossover point (decimal value): {x_value}")
#     print("\nChild After Crossover (One Iteration): ")
#     fitness_values = []
#     for i, chromosome in enumerate(new_population):
#         fitness = calculate_fitness(chromosome)
#         fitness_values.append(fitness)
#         x_value = binary_to_decimal(chromosome)
#         print(f"Chromosome {i+1}: {chromosome} -> X value: {x_value} -> Fitness value: {fitness}")
#     total_fitness = sum(fitness_values)
#     average_fitness = total_fitness / len(population)
#     max_fitness = max(fitness_values)
#     print("Fitness Statistics:")
#     print(f"Sum of fitness values: {total_fitness}")
#     print(f"Average of fitness values: {average_fitness}")
#     print(f"Maximum fitness values: {max_fitness}")
# if __name__ == "__main__":
#     main()


# Mutation
# import random
# POPULATION_SIZE = 6
# CHROMOSOME_LENGTH = 5
# MUTATION_RATE = 0.1
# population = [
#     [0, 1, 1, 0, 1],
#     [0, 1, 1, 0, 1],
#     [0, 1, 1, 0, 1],
#     [0, 1, 1, 1, 1],
#     [0, 1, 0, 1, 1],
#     [1, 1, 0, 0, 1],
# ]
# def binary_to_decimal(binary_chromosome):
#     decimal_value = 0
#     for bit in binary_chromosome:
#         decimal_value = (decimal_value << 1) | bit
#     return decimal_value
# def calculate_fitness(binary_chromosome):
#     x = binary_to_decimal(binary_chromosome)
#     fitness_value = x**2 + 3*x + 5
#     return fitness_value
# def mutate(chromosome):
#     mutated_chromosome = []
#     for bit in chromosome:
#         if random.random() < MUTATION_RATE:
#             mutated_bit = 1-bit
#         else:
#             mutated_bit = bit
#         mutated_chromosome.append(mutated_bit)
#     return mutated_chromosome
# def main():
#     mutated_population = []
#     for chromosome in population:
#         mutated_chromosome = mutate(chromosome)
#         mutated_population.append(mutated_chromosome)
#     print("Child after crossover:")
#     for i, chromosome in enumerate(population):
#         x_value = binary_to_decimal(chromosome)
#         print(f"Chromosome {i+1}: {chromosome} -> X value: {x_value}")
#     print("\nChild after flipping (Mutated Population): ")
#     fitness_values = []
#     for i, chromosome in enumerate(mutated_population):
#         fitness = calculate_fitness(chromosome)
#         fitness_values.append(fitness)
#         x_value = binary_to_decimal(chromosome)
#         print(f"Chromosome {i+1}: {chromosome} -> X value: {x_value} -> Fitness value: {fitness}")
#     total_fitness = sum(fitness_values)
#     average_fitness = total_fitness / len(population)
#     max_fitness = max(fitness_values)
#     print("\nFitness Statistics:")
#     print(f"Sum of fitness values: {total_fitness}")
#     print(f"Average of fitness values: {average_fitness}")
#     print(f"Maximum fitness values: {max_fitness}")
# if __name__ == "__main__":
#     main()
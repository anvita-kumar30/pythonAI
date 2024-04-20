import random

POPULATION_SIZE = 6
GENES = '0123456789'
TARGET = 30
GENE_LENGTH = 4  # Number of genes in each chromosome representing variables a, b, c, d


class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self.calculate_fitness()

    @classmethod
    def create_chromosome(cls):
        return [random.choice(GENES) for _ in range(GENE_LENGTH)]

    def mate(self, partner):
        child_genes = [self.genes[i] if random.random() < 0.5 else partner.genes[i] for i in range(GENE_LENGTH)]
        return Chromosome(child_genes)

    def calculate_fitness(self):
        # Calculate the fitness based on the optimization function F(x)
        total_value = sum((i + 1) * int(gene) for i, gene in enumerate(self.genes))
        return abs(total_value - TARGET)


def initialize_population():
    return [Chromosome(Chromosome.create_chromosome()) for _ in range(POPULATION_SIZE)]


def evolve_population(population):
    iterations = 0

    while iterations < 50:
        population = sorted(population, key=lambda x: x.fitness)

        # Print initial population
        if iterations == 0:
            print("Initial Population:")
            for i, chromosome in enumerate(population, 1):
                print(f"Chromosome {i}: {chromosome.genes}")

        # Check for optimal solution
        if population[0].fitness == 0:
            break

        new_population = []

        # Elitism: Select the top 10% of the population
        new_population.extend(population[:int(0.1 * POPULATION_SIZE)])

        # Crossover: Generate the rest 90% of the new population through mating
        for _ in range(int(0.9 * POPULATION_SIZE)):
            parent1 = random.choice(population[:int(0.5 * POPULATION_SIZE)])
            parent2 = random.choice(population[:int(0.5 * POPULATION_SIZE)])
            child = parent1.mate(parent2)
            new_population.append(child)

        population = new_population
        iterations += 1

    return population


def main():
    # Initialize the population
    population = initialize_population()

    # Evolve the population using genetic algorithm
    final_population = evolve_population(population)

    # Print final population
    print("\nFinal Population:")
    for i, chromosome in enumerate(final_population, 1):
        print(f"Chromosome {i}: {chromosome.genes} (Fitness: {chromosome.fitness})")

    # Find the best chromosome (optimal solution)
    best_chromosome = min(final_population, key=lambda x: x.fitness)
    print(f"\nBest Chromosome (Optimal Solution): {best_chromosome.genes}")
    print(f"Fitness: {best_chromosome.fitness}")
    values = [(i + 1) * int(gene) for i, gene in enumerate(best_chromosome.genes)]
    print(f"Values of ['a', 'b', 'c', 'd']: {values}")


if __name__ == '__main__':
    main()

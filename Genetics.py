import random

POPULATION_SIZE = 7
GENES = '0123456789'
TARGET = 30


class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self.calculate_fitness()

    @classmethod
    def create_chromosome(cls):
        return [random.choice(GENES) for _ in range(4)]

    def mate(self, partner):
        child_genes = [self.genes[i] if random.random() < 0.5 else partner.genes[i] for i in range(4)]
        return Chromosome(child_genes)

    def calculate_fitness(self):
        return abs(sum((i + 1) * int(gene) for i, gene in enumerate(self.genes)) - TARGET)


def main():
    population = [Chromosome(Chromosome.create_chromosome()) for _ in range(POPULATION_SIZE)]
    iterations = 0

    while iterations < 50:
        population = sorted(population, key=lambda x: x.fitness)
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

    # Print the initial and final chromosomes
    print("Initial Chromosomes:")
    for i, chromosome in enumerate(population, 1):
        print(f"Chromosome {i}: {chromosome.genes}")

    print("\nFinal Chromosomes:")
    for i, chromosome in enumerate(population, 1):
        print(f"Chromosome {i}: {chromosome.genes}")

    # Print the best solution and values of a, b, c, d
    best_chromosome = population[0]
    print(f"\nBest Chromosome: {best_chromosome.genes}")
    print(f"Best Solution: {TARGET - best_chromosome.fitness}")
    print(f"Values of ['a', 'b', 'c', 'd']: {tuple(int(gene) for gene in best_chromosome.genes)}")
    print(f"Number of Iterations: {iterations}")


if __name__ == '__main__':
    main()

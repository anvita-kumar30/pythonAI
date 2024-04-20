import random

POPULATION_SIZE = 6
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
        # Single-point crossover
        crossover_point = random.randint(0, 3)
        child_genes = self.genes[:crossover_point] + partner.genes[crossover_point:]
        return Chromosome(child_genes)

    def mutate(self):
        # Random mutation
        mutate_index = random.randint(0, 3)
        self.genes[mutate_index] = random.choice(GENES)

    def calculate_fitness(self):
        # Calculate fitness as negative absolute difference from target
        a, b, c, d = map(int, self.genes)
        value = (a + 2*b + 3*c + 4*d)
        return -abs(value - TARGET)


def initial_population():
    return [Chromosome(Chromosome.create_chromosome()) for _ in range(POPULATION_SIZE)]


def tournament_selection(population, tournament_size=2):
    tournament_contestants = random.sample(population, tournament_size)
    winner = max(tournament_contestants, key=lambda x: x.fitness)
    return winner


def genetic_algorithm():
    population = initial_population()
    iterations = 0

    while iterations < 50:
        population = sorted(population, key=lambda x: x.fitness)

        best_chromosome = population[0]
        if best_chromosome.fitness == 0:
            break

        new_population = []

        # Elitism: Select the top 10% of the population
        new_population.extend(population[:int(0.1 * POPULATION_SIZE)])

        # Crossover: Generate the rest 90% of the new population through mating
        for _ in range(int(0.9 * POPULATION_SIZE)):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child = parent1.mate(parent2)
            if random.random() < 0.1:  # 10% chance of mutation
                child.mutate()
            new_population.append(child)

        population = new_population
        iterations += 1

    # Print initial and final populations
    print("Initial Population:")
    for i, chromosome in enumerate(population, 1):
        print(f"Chromosome {i}: {chromosome.genes}")

    print("\nFinal Population:")
    for i, chromosome in enumerate(population, 1):
        print(f"Chromosome {i}: {chromosome.genes}")

    # Find and print the best chromosome (optimal solution)
    best_chromosome = min(population, key=lambda x: -x.fitness)
    print("\nBest Chromosome (Optimal Solution):")
    print(f"Genes: {best_chromosome.genes}")
    print(f"Fitness: {-best_chromosome.fitness}")


if __name__ == '__main__':
    genetic_algorithm()

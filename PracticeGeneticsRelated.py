# Genetics
import random
POPULATION_SIZE = 6
GENES = [str(i) for i in range(10)]
TARGET = 30
MAX_ITERATIONS = 50
class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = self.calculate_fitness()
    def calculate_fitness(self):
        a, b, c, d = [int(gene) for gene in self.genes]
        return abs((a + 2*b + 3*c + 4*d) - 30)
    def crossover(self, other):
        crossover_point = random.randint(1, len(self.genes) - 1)
        child_genes = (
            self.genes[:crossover_point] +
            other.genes[crossover_point:]
        )
        return Chromosome(child_genes)
    def mutate(self):
        mutated_gene_indices = random.sample(range(len(self.genes)), random.randint(1,2))
        mutated_genes = [
            random.choice(GENES) if idx in mutated_gene_indices else gene
            for idx, gene in enumerate(self.genes)
        ]
        return Chromosome(mutated_genes)
def selection(population):
    sorted_population = sorted(population, key=lambda x: x.fitness)
    return sorted_population[:2]
def main():
    population = [
        Chromosome(['10', '12', '22', '43']),
        Chromosome(['2', '54', '11', '22']),
        Chromosome(['14', '8', '9', '12']),
        Chromosome(['9', '4', '32', '32']),
        Chromosome(['32', '12', '1', '21']),
        Chromosome(['4', '98', '9', '6'])
    ]
    print("Initial Chromosomes: ")
    for i, chromosome in enumerate(population, 1):
        print(f"Chromosome {i}: {chromosome.genes}")
    iteration = 0
    best_solution = None
    while iteration < MAX_ITERATIONS:
        parent1, parent2 = selection(population)
        child = parent1.crossover(parent2)
        child = child.mutate()
        population.remove(max(population, key=lambda x: x.fitness))
        population.append(child)
        best_chromosome = min(population, key=lambda x: x.fitness)
        if best_solution is None or best_chromosome.fitness < best_solution.fitness:
            best_solution = best_chromosome
        iteration += 1
    print("\nFinal Chromosomes: ")
    for i, chromosome in enumerate(population, 1):
        print(f"Chromosome {i}: {chromosome.genes}")
    print(f"\nBest Chromosome: {best_solution.genes}")
    print(f"Best Solution: {sum((i+1)*int(gene) for i, gene in enumerate(best_solution.genes))}")
    print(f"Values of a, b, c, d: {tuple(int(gene) for gene in best_solution.genes)}")
    print(f"Number of iterations: {iteration}")
if __name__ == "__main__":
    main()

# Crossover


# Mutation
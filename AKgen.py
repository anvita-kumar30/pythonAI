import random

# Define the optimization function F(x)
def fitness_function(chromosome):
    a, b, c, d = chromosome
    return abs((a + 2*b + 3*c + 4*d) - 30)

# Initialize the population
def initialize_population(population_size):
    population = []
    for _ in range(population_size):
        chromosome = [random.randint(0, 30) for _ in range(4)] # Randomly generate chromosome
        population.append(chromosome)
    return population

# Selection: Tournament selection
def tournament_selection(population, tournament_size):
    selected_parents = []
    for _ in range(2): # Select 2 parents
        tournament = random.sample(population, tournament_size) # Randomly select tournament participants
        best_chromosome = min(tournament, key=fitness_function) # Choose the participant with the lowest fitness
        selected_parents.append(best_chromosome)
    return selected_parents

# Crossover: Single-point crossover
def crossover(parent1, parent2, crossover_rate):
    if random.random() > crossover_rate:
        return parent1, parent2
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation: Bit flip mutation
def mutation(child, mutation_rate):
    mutated_child = []
    for gene in child:
        if random.random() < mutation_rate:
            mutated_gene = random.randint(0, 30)
            mutated_child.append(mutated_gene)
        else:
            mutated_child.append(gene)
    return mutated_child

# Genetic Algorithm
def genetic_algorithm(population_size, tournament_size, crossover_rate, mutation_rate):
    population = initialize_population(population_size)
    iteration = 0
    print("Initial Population:")
    print(population)
    for generation in range(1000):
        new_population = []
        iteration += 1
        while len(new_population) < population_size:
            parent1, parent2 = tournament_selection(population, tournament_size)
            child1, child2 = crossover(parent1, parent2, crossover_rate)
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            new_population.extend([child1, child2])
        population = new_population
        best_chromosome = min(population, key=fitness_function)
        if fitness_function(best_chromosome) == 0: # Terminate if the optimal solution is found
            break
    return best_chromosome, iteration

# Example usage
if __name__ == "__main__":
    population_size = 6
    tournament_size = 3
    crossover_rate = 0.8
    mutation_rate = 0.1
    best_solution, iterations = genetic_algorithm(population_size, tournament_size, crossover_rate, mutation_rate)
    print("Optimal Solution Found:", best_solution)
    print("Number of Iterations:", iterations)
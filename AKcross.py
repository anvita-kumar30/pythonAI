import random

# Function to convert decimal to binary
def decimal_to_binary(decimal):
    return bin(decimal)[2:]

# Input 6 chromosomes in decimal form
chromosomes_decimal = [31, 48, 51, 57, 21, 14]

# Convert chromosomes to binary
population = [decimal_to_binary(chromosome) for chromosome in chromosomes_decimal]
print(population)

def crossover(parent1, parent2):
    # Randomly choose a crossover point
    crossover_point = random.randint(1, len(parent1) - 1)
    # Perform crossover
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

crossover_rate = 0.25
num_crossovers = int(len(population) * crossover_rate)

for _ in range(num_crossovers):
    # Select two parents randomly
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    # Perform crossover
    child1, child2 = crossover(parent1, parent2)
    # Replace parents with children
    population.remove(parent1)
    population.remove(parent2)
    population.extend([child1, child2])

print("Population after crossover:")
print(population)
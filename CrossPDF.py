import random

# Chromosome Population
chromosomes = [
    [2, 21, 18, 3],
    [10, 4, 13, 14],
    [12, 5, 23, 8],
    [20, 5, 17, 1],
    [10, 4, 13, 14],
    [20, 1, 10, 6]
]

# Randomly generated values for each chromosome
random_values = [0.191, 0.259, 0.76, 0.006, 0.159, 0.34]

# Initialize variables
crossover_rate = 0.25
selected_chromosomes = []
crossover_pairs = []

# Select chromosomes for crossover based on crossover rate
for i, r in enumerate(random_values, 1):
    if r < crossover_rate:
        selected_chromosomes.append(i)

print("Initial Chromosome Population:")
for i, chrom in enumerate(chromosomes, 1):
    print(f"Chromosome {i}: {chrom}")

print("\nRandomly generated values for each chromosome:")
for i, r in enumerate(random_values, 1):
    print(f"R[{i}] = {r}")

print("\nChromosomes selected for crossover:")
for chrom_num in selected_chromosomes:
    print(f"Chromosome {chrom_num} (R[{chrom_num}] < {crossover_rate})")

# Perform crossover
for i in range(len(selected_chromosomes)):  # Loop through all selected chromosomes
    parent1_index = selected_chromosomes[i] - 1
    parent2_index = random.choice(selected_chromosomes) - 1  # Choose a random second parent

    # Select random crossover point
    crossover_point = random.randint(1, len(chromosomes[parent1_index]) - 1)

    # Perform crossover
    crossover_pair = (parent1_index, parent2_index, crossover_point)
    crossover_pairs.append(crossover_pair)
    chrom1 = chromosomes[parent1_index][:crossover_point] + chromosomes[parent2_index][crossover_point:]
    chrom2 = chromosomes[parent2_index][:crossover_point] + chromosomes[parent1_index][crossover_point:]
    chromosomes[parent1_index] = chrom1
    chromosomes[parent2_index] = chrom2

print("\nCrossover Pairs:")
for i, (p1, p2, cp) in enumerate(crossover_pairs, 1):
    print(f"Crossover {i}: Chromosome {p1 + 1} >< Chromosome {p2 + 1}, Cut point: {cp}")

print("\nResulting Chromosomes after crossover:")
for i, (p1, p2, _) in enumerate(crossover_pairs, 1):  # Loop through all crossover pairs
    print(f"Chromosome {p1 + 1} >< Chromosome {p2 + 1}:")
    print(f"Resulting Chromosome {p1 + 1}: {chromosomes[p1]}")
    print(f"Resulting Chromosome {p2 + 1}: {chromosomes[p2]}")

print("\nFinal Resulting Chromosomes:")
for i, chrom in enumerate(chromosomes, 1):
    print(f"Chromosome {i}: {chrom}")
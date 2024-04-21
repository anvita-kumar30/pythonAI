import random

# Function to convert decimal value to binary list
def decimal_to_binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(5)]

# Function to convert binary list to decimal value
def binary_to_decimal(binary):
    return int(''.join(str(bit) for bit in binary), 2)

# Objective function
def objective_function(chromosome):
    return abs(sum((i + 1) * gene for i, gene in enumerate(chromosome)) - 30)

# Chromosome Population
chromosomes = [
    [2, 5, 17, 1],
    [10, 4, 13, 14],
    [12, 5, 23, 8],
    [20, 4, 13, 14],
    [10, 5, 18, 3],
    [20, 1, 10, 6]
]

# Mutation rate
mutation_rate = 0.1

# Calculate the total length of gen in the population
total_gen = len(chromosomes) * len(chromosomes[0])

# Calculate the number of mutations
num_mutations = int(mutation_rate * total_gen)

# Generate random positions for mutations
mutation_positions = random.sample(range(1, total_gen + 1), num_mutations)

print("Mutation Positions:", mutation_positions)

# Perform mutation
for position in mutation_positions:
    # Find the chromosome and gen index based on the position
    chromosome_index = (position - 1) // len(chromosomes[0])
    gen_index = (position - 1) % len(chromosomes[0])

    # Convert the decimal gen value to binary
    binary_gen = decimal_to_binary(chromosomes[chromosome_index][gen_index])

    # Generate a new binary value for the mutated gen
    mutated_bit = random.randint(0, 1)

    # Perform mutation by flipping one random bit
    binary_gen[mutated_bit] = 1 - binary_gen[mutated_bit]

    # Convert the binary gen value back to decimal
    new_value = binary_to_decimal(binary_gen)

    # Update the chromosome with the mutated value
    chromosomes[chromosome_index][gen_index] = new_value

print("\nChromosomes after mutation:")
for i, chrom in enumerate(chromosomes, 1):
    print(f"Chromosome {i}: {chrom}")
    print(f"Objective Function Value: {objective_function(chrom)}")
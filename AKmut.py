import random

# Function to convert decimal to binary
def decimal_to_binary(decimal):
    return bin(decimal)[2:]

# Input 6 chromosomes in decimal form
chromosomes_decimal = [30, 45, 51, 57, 21, 14]

# Convert chromosomes to binary
population = [decimal_to_binary(chromosome) for chromosome in chromosomes_decimal]
print(population)

mutation_rate = 0.1

def mutation(chromosome, mutation_rate):
    mutated_chromosome = ""
    for gene in chromosome:
        # Check if mutation should occur for this gene
        if random.random() < mutation_rate:
            # Flip the bit (mutation)
            if gene == '1':
                mutated_chromosome += '0'
            else:
                mutated_chromosome += '1'
        else:
            mutated_chromosome += gene
    return mutated_chromosome

# Perform mutation on each chromosome in the population
for i in range(len(population)):
    population[i] = mutation(population[i], mutation_rate)

print("Population after mutation:")
print(population)
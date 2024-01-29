import random

population_size = 100
string_length = 30
mutation_rate = 0.01
generations = 50

def create_individual(length):
    return[random.choice([0,1]) for _ in range(length)]

def calculate_fitness(individual):
    return sum(individual)

def mutate(individual, mutation_rate):
    mutated_individual = []
    for gene in individual:
        if random.random() < mutation_rate:
            mutated_individual.append(1-gene)
        else:
            mutated_individual.append(gene)
    return mutated_individual

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1)-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def genetic_algorithm(population_size, string_length, mutation_rate, generations):
    population = [create_individual(string_length) for _ in range(population_size)]

    for generation in range(generations):

        fitness_scores = [calculate_fitness(individual) for individual in population]

        parents = random.choices(population, weights=fitness_scores, k=2)

        new_generation = [mutate(crossover(*parents), mutation_rate)for _ in range(population_size)]

        population = new_generation

        best_individual = max(population, key=calculate_fitness)
        print(f"Generation {generation +1}, Best Fitness {calculate_fitness(best_individual)}")

        return population


final_population = genetic_algorithm(population_size, string_length, mutation_rate, generations)
best_individual =  max(final_population, key=calculate_fitness)

print("Best Individual:", best_individual)
print("Fitness: ", calculate_fitness(best_individual))
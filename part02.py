import random
import matplotlib.pyplot as plt

population_size = 100
string_length = 30
mutation_rate = 0.01
generations = 50
target_string = [1,1,1,0,0,1,0,1,1,0,0,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0]

def create_individual(length):
    return[random.choice([0,1]) for _ in range(length)]

def calculate_fitness(individual, target_string):
    return sum(1 for i, j in zip(individual, target_string)if i == j)

def mutate(individual, mutation_rate):
    mutated_individual = [1 - gene if random.random() < mutation_rate else gene for gene in individual]
    return mutated_individual

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1)-1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def genetic_algorithm(population_size, string_length, mutation_rate, generations, target_string):
    population = [create_individual(string_length) for _ in range(population_size)]
    average_fitness_list = []

    for generation in range(generations):

        fitness_scores = [calculate_fitness(individual, target_string) for individual in population]

        average_fitness = sum(fitness_scores) / len(fitness_scores)
        average_fitness_list.append(average_fitness)

        parents = random.choices(population, weights=fitness_scores, k=2)

        new_generation = [mutate(crossover(*parents), mutation_rate)for _ in range(population_size)]

        population = new_generation

        print(f"Generation {generation + 1}, Average Fitness: {average_fitness}")

    plt.plot(range(1, generations + 1), average_fitness_list, marker='o')
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness Over Generations (Part 2)')
    plt.show()

    return population


final_population = genetic_algorithm(population_size, string_length, mutation_rate, generations, target_string)
best_individual = max(final_population, key=lambda ind: calculate_fitness(ind, target_string))

print("Best Individual:", best_individual)
print("Fitness: ", calculate_fitness(best_individual, target_string))
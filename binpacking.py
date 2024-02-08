import random
import matplotlib.pyplot as plt

bP1 = """
BPP 1
46
1000
200 3
199 1
198 2
197 2
194 2
193 1
192 1
191 3
190 2
189 1
188 2
187 2
186 1
185 4
184 3
183 3
182 3
181 2
180 1
179 4
178 1
177 4
175 1
174 1
173 2
172 1
171 3
170 2
169 3
167 2
165 2
164 1
163 4
162 1
161 1
160 2
159 1
158 3
157 1
156 6
155 3
154 2
153 1
152 3
151 2
150 4
"""

lines = bP1.strip().split('\n')
title = lines[0]
binCapacity = int(lines[1])
itemWeights = [(int(line.split()[0]), int(line.split()[1])) for line in lines[3:]]

population_size = 100
mutation_rate = 0.01
generations = 50

def create_individual(itemWeights):
    return[random.choice([0,1]) for _ in range(len(itemWeights))]

def calculate_fitness(individual, itemWeights):
    totalWeight = sum(itemWeights[i][0] for i in range(len(individual)) if individual[i] ==1)
    return 1 if totalWeight <= binCapacity else 0

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

def genetic_algorithm(population_size, itemWeights, mutation_rate, generations):
    population = [create_individual(itemWeights) for _ in range(population_size)]
    average_fitness_list = []

    for generation in range(generations):

        fitness_scores = [calculate_fitness(individual,itemWeights) for individual in population]

        average_fitness = sum(fitness_scores)/len(fitness_scores)
        average_fitness_list.append(average_fitness)

        parents = random.choices(population, weights=fitness_scores, k=2)

        new_generation = [mutate(crossover(*parents), mutation_rate)for _ in range(population_size)]

        population = new_generation

        best_individual = max(population, key=lambda ind: calculate_fitness(ind,itemWeights))
        print(f"Generation {generation +1}, Best Fitness {calculate_fitness(best_individual)}")

    plt.plot(range(1, generations + 1), average_fitness_list, marker='o')
    plt.xlabel('Generation')
    plt.ylabel('Average Fitness')
    plt.title('Average Fitness Over Generations (Part 1)')
    plt.show()

    return population


final_population = genetic_algorithm(population_size, itemWeights, mutation_rate, generations)
best_individual = max(final_population, key=lambda ind: calculate_fitness(ind, itemWeights))

print("Best Individual:", best_individual)
print("Fitness: ", calculate_fitness(best_individual))
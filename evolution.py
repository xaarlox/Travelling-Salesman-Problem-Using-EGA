import random

from crossover import ordered_crossover
from mutation import mutate
from selection import tournament_selection
from utils import calc_distance


# evolve_population проводить селекцію, схрещування та мутацію, щоб покращити рішення з кожним новим поколінням
def evolve_population(population, tournament_size, mutation_rate, crossover_rate, elitism=True):
    new_population = []
    sorted_pop = sorted(population)

    if elitism:
        new_population.extend(sorted_pop[:2])  # Тут зберігаємо дві найкращі особини

    while len(new_population) < len(population):
        parent1 = tournament_selection(population, tournament_size)[1]
        parent2 = tournament_selection(population, tournament_size)[1]

        if random.random() < crossover_rate:
            child1 = ordered_crossover(parent1, parent2)
            child2 = ordered_crossover(parent2, parent1)
        else:
            child1, child2 = parent1[:], parent2[:]
        child1 = mutate(child1, mutation_rate)
        child2 = mutate(child2, mutation_rate)

        new_population.append((calc_distance(child1), child1))
        if len(new_population) < len(population):
            new_population.append((calc_distance(child2), child2))
    return sorted(new_population)

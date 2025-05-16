import random
from utils import calc_distance


# Файл містить функцію select_population, яка генерує початкову популяцію можливих маршрутів для елітного генетичного алгоритму
def select_population(cities, size):
    population = []
    for i in range(size):
        c = cities.copy()
        random.shuffle(c)
        distance = calc_distance(c)
        population.append([distance, c])
    return sorted(population)

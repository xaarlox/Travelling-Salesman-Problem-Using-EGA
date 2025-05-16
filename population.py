import random
from utils import calc_distance


# Файл містить функцію select_population, яка генерує початкову популяцію можливих маршрутів для елітного генетичного алгоритму
def select_population(cities, size, quality=5):
    multiplier = 1 + (quality - 5) * 0.2
    generated_size = int(size * multiplier)

    population = []
    for i in range(generated_size):
        c = cities.copy()
        random.shuffle(c)
        distance = calc_distance(c)
        population.append((distance, c))
    population = sorted(population)
    return population[:size]

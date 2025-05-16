import math


# Файл містить функцію calc_distance, яка обчислює загальну відстань для заданого маршруту між містами
def calc_distance(cities):
    total_sum = 0
    for i in range(len(cities)):
        city_a = cities[i]
        city_b = cities[(i + 1) % len(cities)]
        total_sum += math.hypot(city_b[1] - city_a[1], city_b[2] - city_a[2])
    return total_sum


# Функція, яка приймає введені дані від користувача
def get_user_input():
    pop_size = int(input("Population size: "))
    tournament_size = int(input("Tournament size: "))
    mutation_rate = float(input("Mutation rate (0.0 - 1.0): "))
    crossover_rate = float(input("Crossover rate (0.0 - 1.0): "))
    quality = int(input("Quality of the initial population (1 - 10): "))
    quality = max(1, min(10, quality))
    max_gen_input = input("Maximum number of generations (enter -1 for 'to the last living'): ").strip()
    max_generations = int(max_gen_input)
    stop_if_no_improve = int(input("Stop if there is no improvement for N generations: "))

    return {
        "pop_size": pop_size,
        "tournament_size": tournament_size,
        "mutation_rate": mutation_rate,
        "crossover_rate": crossover_rate,
        "quality": quality,
        "max_generations": max_generations,
        "stop_if_no_improve": stop_if_no_improve
    }

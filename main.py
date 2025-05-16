import matplotlib.pyplot as plt

from evolution import evolve_population
from population import select_population
from utils import get_user_input


# Функція, котра завантажує координати міст з текстового файлу
def load_cities(filepath):
    with open(filepath) as f:
        return [
            [int(parts[0]), float(parts[1]), float(parts[2])]
            for parts in (line.split() for line in f)
        ]


# Візуалізація міст: точки міст з'єднані лініями
def draw_map(route):
    for city in route:
        plt.plot(city[1], city[2], "ro")
        plt.annotate(city[0], (city[1], city[2]))

    for i in range(len(route)):
        a = route[i]
        b = route[(i + 1) % len(route)]
        plt.plot([a[1], b[1]], [a[2], b[2]], "gray")

    plt.show()


# Основна функція для запуску генетичного алгоритму
def run_ga(pop_size, tournament_size, mutation_rate, crossover_rate, quality, max_generations,
           stop_if_no_improve):
    filepath = "TSP51.txt"
    cities = load_cities(filepath)
    population = select_population(cities, pop_size, quality)
    best = population[0]
    no_improve = 0
    generation = 0

    while max_generations == -1 or generation < max_generations:
        generation += 1
        population = evolve_population(population, tournament_size, mutation_rate, crossover_rate)
        if population[0][0] < best[0]:
            best = population[0]
            no_improve = 0
        else:
            no_improve += 1
        avg = sum(p[0] for p in population) / len(population)
        print(f"Generation {generation}: Best distance = {population[0][0]:.2f}, Mean = {avg:.2f}")
        if no_improve >= stop_if_no_improve:
            print("Stopping: no improvement over", stop_if_no_improve, "generations.")
            break

    print(f"\nBest found distance: {best[0]}, Generation: {generation}")
    draw_map(best[1])


if __name__ == "__main__":
    params = get_user_input()
    run_ga(**params)

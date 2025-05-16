import random


# Функція, яка реалізує мутацію маршруту
def mutate(route, mutation_rate):
    new_route = route[:]
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

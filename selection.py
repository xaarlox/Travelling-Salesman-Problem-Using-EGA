import random


# Функція, яка реалізовує турнірний відбір
def tournament_selection(population, k):
    return min(random.choices(population, k=k), key=lambda x: x[0])

import random


# Дана функція реалізує оператор схрещування
def ordered_crossover(paren1, parent2):
    size = len(paren1)
    start = random.randint(0, size - 1)
    end = random.randint(start, size - 1)

    child = [None] * size
    child[start:end + 1] = paren1[start:end + 1]
    pointer = 0
    for gene in parent2:
        if gene not in child:
            while child[pointer] is not None:
                pointer += 1
            child[pointer] = gene
    return child

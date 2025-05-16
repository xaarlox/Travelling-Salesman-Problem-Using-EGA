import math


# Файл містить функцію calc_distance, яка обчислює загальну відстань для заданого маршруту між містами
def calc_distance(cities):
    total_sum = 0
    for i in range(len(cities)):
        city_a = cities[i]
        city_b = cities[(i + 1) % len(cities)]
        total_sum += math.hypot(city_b[1] - city_a[1], city_b[2] - city_a[2])
    return total_sum

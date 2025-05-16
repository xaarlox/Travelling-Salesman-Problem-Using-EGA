import unittest
from population import select_population
from utils import calc_distance
from mutation import mutate
from crossover import ordered_crossover
from selection import tournament_selection
from evolution import evolve_population

# Тестові міста
CITIES = [
    [0, 0.0, 0.0],
    [1, 1.0, 0.0],
    [2, 0.0, 1.0]
]


class TestGeneticAlgorithm(unittest.TestCase):
    # calc_distance (обчислення сумарної довжини маршруту для трикутної конфігурації міст)
    def test_calc_distance_triangle(self):
        expected = 1 + (2 ** 0.5) + 1
        result = calc_distance(CITIES)
        self.assertAlmostEqual(result, expected, places=6)

    # select_population (чи вона створює популяцію правильної величини та чи всі маршрути мають коректну довжину)
    def test_select_population_size_and_validity(self):
        population = select_population(CITIES, size=10, quality=5)
        self.assertEqual(len(population), 10)
        for dist, route in population:
            self.assertEqual(len(route), len(CITIES))
            self.assertEqual(sorted([c[0] for c in route]), [0, 1, 2])
            self.assertIsInstance(dist, float)

    # ordered_crossover (правильне створення нащадка на основі двох батьківських маршрутів, зберігаючи всі початкові місця)
    def test_ordered_crossover_valid_output(self):
        parent1 = CITIES
        parent2 = list(reversed(CITIES))
        child = ordered_crossover(parent1, parent2)
        self.assertEqual(sorted([c[0] for c in child]), [0, 1, 2])
        self.assertEqual(len(child), len(CITIES))

    # mutate (чи правильно змінює порядок міст у маршруті, але не втрачає жодного з них)
    def test_mutation_preserves_genes(self):
        original = CITIES
        mutated = mutate(original, mutation_rate=1.0)
        self.assertEqual(sorted([c[0] for c in mutated]), sorted([c[0] for c in original]))
        self.assertEqual(len(mutated), len(original))
        self.assertNotEqual(mutated, original)

    # tournament_selection (чи правильно вибирає батьків для наступного покоління)
    def test_tournament_selection_returns_valid_parent(self):
        population = [(10.0, ["A"]), (5.0, ["B"]), (15.0, ["C"])]
        selected = tournament_selection(population, k=2)
        self.assertIn(selected, population)

    # Чи функція evolve_population підтримує розмір популяції та чи всі її маршрути залишаються коректними
    def test_evolve_population_returns_same_size_and_valid(self):
        population = select_population(CITIES, size=10, quality=5)
        evolved = evolve_population(population, tournament_size=2,
                                    mutation_rate=0.5, crossover_rate=0.8)
        self.assertEqual(len(evolved), len(population))
        for fit, route in evolved:
            self.assertIsInstance(fit, float)
            self.assertEqual(sorted([c[0] for c in route]), [0, 1, 2])


if __name__ == "__main__":
    unittest.main()

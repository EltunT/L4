#Задание 1

from itertools import combinations

def find_combinations(items, backpack_size, initial_score):
    all_combinations = []
    for r in range(1, backpack_size + 1):
        for combo in combinations(items.keys(), r):
            total_size = sum(items[item]['size'] for item in combo)
            total_value = sum(items[item]['value'] for item in combo)
            if total_size <= backpack_size:
                all_combinations.append((combo, total_value - total_size))
    viable_combinations = [combo for combo in all_combinations if combo[1] + initial_score > 0]
    return viable_combinations

def sort_combinations_by_value(combinations):
    sorted_combinations = [(total_value, items_list) for items_list, total_value in combinations]
    sorted_combinations.sort(reverse=True)
    return [(items_list, total_value) for total_value, items_list in sorted_combinations]

def print_combinations(viable_combinations):
    for combo in viable_combinations:
        items_list = ', '.join(combo[0])
        total_value = combo[1]
        print(f"[{items_list}] — Итоговые очки выживания: {total_value}")

items = {
    'r': {'size': 3, 'value': 25},
    'p': {'size': 2, 'value': 15},
    'a': {'size': 2, 'value': 15},
    'm': {'size': 2, 'value': 20},
    'i': {'size': 1, 'value': 5},
    'k': {'size': 1, 'value': 15},
    'x': {'size': 3, 'value': 20},
    't': {'size': 1, 'value': 25},
    'f': {'size': 1, 'value': 15},
    'd': {'size': 1, 'value': 10},
    's': {'size': 2, 'value': 20},
    'c': {'size': 2, 'value': 20}
}

backpack_size = 7
initial_score = 15

viable_combinations = find_combinations(items, backpack_size, initial_score)
sorted_viable_combinations = sort_combinations_by_value(viable_combinations)
print_combinations(sorted_viable_combinations[:5])

#Задание 2_1вариант(с использованием фун-ий из первого задания)

def find_optimal_combinations_for_2x4(items, initial_score):
    backpack_size = 8
    all_combinations = []

    for r in range(1, backpack_size + 1):
        for combo in combinations(items.keys(), r):
            total_size = sum(items[item]['size'] for item in combo)
            total_value = sum(items[item]['value'] for item in combo)
            if total_size == backpack_size:
                all_combinations.append((combo, total_value - total_size))

    viable_combinations = [combo for combo in all_combinations if combo[1] + initial_score > 0]
    return viable_combinations

viable_combinations_variant1 = find_optimal_combinations_for_2x4(items, 15)
sorted_viable_combinations_variant1 = sort_combinations_by_value(viable_combinations_variant1)
print_combinations(sorted_viable_combinations_variant1[:5])

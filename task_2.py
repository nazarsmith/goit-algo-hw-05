from searchers import binary_search

import random
import numpy as np


def make_test_data(num_items: int = 100):
    test_data = np.linspace(-10, 10, num_items)
    return test_data


def run_tests(num_items, to_find: int = None):
    if isinstance(num_items, list):
        test_data = num_items
    else:
        test_data = make_test_data(num_items)
    print(test_data)
    if to_find:
        sought_item = to_find
    else:
        sought_item = random.choice(test_data)
    print(f"\nItem to find: {sought_item}")
    sorted_list = sorted(test_data)
    index, iterations = binary_search(sorted_list, sought_item)
    # return sorted_list[index], tuple([iterations, sorted_list[high]])
    return iterations, sorted_list[index]


# results = run_tests(20)
target = -1
results = run_tests(50, target)
print(
    f"Raw result: {results}",
    f"Results type: {type(results)}",
    f"Number of iterations it took: {results[0]}",
    f"Item found: {results[1] == target}",
    f"The upper limit of the search: {results[1]}",
    sep="\n",
    end="\n" * 2,
)

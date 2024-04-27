from searchers import binary_search

import random
import numpy as np


def make_test_data(num_items=100):
    test_data = np.linspace(-10, 10, num_items)
    return test_data


def run_tests(num_items):
    test_data = make_test_data(num_items)
    sought_item = random.choice(test_data)
    print(f"\nItem to find: {sought_item}")
    sorted_list = sorted(test_data)
    index, iterations, high = binary_search(sorted_list, sought_item)
    return sorted_list[index], tuple([iterations, sorted_list[high]])


results = run_tests(1000)
print(
    f"Results type: {type(results)}",
    f"Number of iterations it took: {results[1][0]}",
    f"Actual item found: {results[0]}",
    f"The upper limit of the search: {results[1][1]}",
    sep="\n",
    end="\n" * 2,
)

from searchers import *
from functools import partial

import matplotlib.pyplot as plt
import timeit


def load_text(text_path: str):
    with open(text_path, "r") as file:
        text = file.read()
    return text


def run_tests_for_text(text: str, pattern: str):
    test_data = load_text(text)
    kmp = partial(kmp_search, text=test_data, pattern=pattern)
    boyer_moore = partial(boyer_moore_search, text=test_data, pattern=pattern)
    rabin_karp = partial(rabin_karp_search, text=test_data, pattern=pattern)

    kmp_time = timeit.timeit(stmt=kmp, number=20)
    boyer_moore_time = timeit.timeit(stmt=boyer_moore, number=20)
    rabin_karp_time = timeit.timeit(stmt=rabin_karp, number=20)

    print(
        f"{kmp_time} using Knuth–Morris–Pratt algorithm;",
        f"{boyer_moore_time} using Boyer-Moore algorithm;",
        f"{rabin_karp_time} using Rabin-Karp algorithm.\n",
        sep="\n",
    )

    return {
        "KMP": kmp_time,
        "Boyer-Moore": boyer_moore_time,
        "Rabin-Karp": rabin_karp_time,
    }


print("\nThe time it took to find a substring in text_1:")
success_text_1 = run_tests_for_text(
    "C:\Projects\\algorithms\goit-algo-hw-05\\text_1.txt", "ніж поточний"
)
print(success_text_1)
print("\nThe time it took to find a substring in text_2:")
success_text_2 = run_tests_for_text(
    "C:\Projects\\algorithms\goit-algo-hw-05\\text_2.txt", "елементу здійснюється"
)
print(success_text_2)
print("\nThe time it took to go through text_1 and fail to find the substring:")
fail_text_1 = run_tests_for_text(
    "C:\Projects\\algorithms\goit-algo-hw-05\\text_1.txt", "ніжпо"
)
print(fail_text_1)
print("\nThe time it took to go through text_2 and fail to find the substring:")
fail_text_2 = run_tests_for_text(
    "C:\Projects\\algorithms\goit-algo-hw-05\\text_2.txt", "уякі"
)
print(fail_text_2)

labels = list(success_text_1.keys())
success_values_1 = list(success_text_1.values())
success_values_2 = list(success_text_2.values())

plt.bar(labels, success_values_1, color="b", alpha=0.7, width=0.2)
plt.bar(labels, success_values_2, color="r", alpha=0.7, width=0.2)
# ins, = plt.plot(
#     [
#         low_data[1], low_mid_data[1], mid_data[1], mid_large_data[1], large_data[1], large_very_large_data[1], very_large_data[1]
#     ],
#     color = "r",
#     alpha = 0.7,
#     label = "Insert"
#     )
# srt, = plt.plot(
#     [
#         low_data[2], low_mid_data[2], mid_data[2], mid_large_data[2], large_data[2], large_very_large_data[2], very_large_data[2]
#     ],
#     color = "g",
#     alpha = 0.7,
#     label = "sorted()"
#     )
# plt.xlabel('Num experiments')
# plt.ylabel('Seconds')
# plt.legend(handles = [mr, ins, srt])
plt.show()

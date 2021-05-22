import random
import sys

import pandas as pd
import matplotlib.pyplot as plt

from sorting_functions_project.quicksort import quick_sort
from sorting_functions_project.heapsort import heap_sort
from sorting_functions_project.selection_sort import selection_sort
from sorting_functions_project.time_measure import time_measure

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

sys.setrecursionlimit(1000000)

quick_sort_sort_time = []
heap_sort_sort_time = []
selection_sort_sort_time = []

sum_quick_sort_time = 0
sum_heap_sort_time = 0
sum_selection_sort_time = 0

A_before_sort = []
for num in range(5000):
    x = random.randint(0, 10)
    A_before_sort.append(x)

A_after_sort = A_before_sort.copy()
B_after_sort = A_before_sort.copy()
C_after_sort = A_before_sort.copy()

measure_time_quick_sort_unsorted, quick_sort_sorted_table = time_measure(quick_sort, A_after_sort, 0, len(A_after_sort) - 1)
measure_time_heap_sort_unsorted, heap_sort_sorted_table = time_measure(heap_sort, B_after_sort)
measure_time_selection_sort_unsorted, selection_sort_sorted_table = time_measure(selection_sort, C_after_sort)

measure_time_quick_sort_sorted, _ = time_measure(quick_sort, quick_sort_sorted_table, 0, len(quick_sort_sorted_table) - 1)
measure_time_heap_sort_sorted, _ = time_measure(heap_sort, heap_sort_sorted_table)
measure_time_selection_sort_sorted, _ = time_measure(selection_sort, selection_sort_sorted_table)

quick_sort_reverse_table = quick_sort_sorted_table.copy()
heap_sort_reverse_table = heap_sort_sorted_table.copy()
selection_sort_reverse_table = selection_sort_sorted_table.copy()

quick_sort_reverse_table.reverse()
heap_sort_reverse_table.reverse()
selection_sort_reverse_table.reverse()

measure_time_quick_sort_reverse_sorted, _ = time_measure(quick_sort, quick_sort_reverse_table, 0, len(quick_sort_reverse_table) - 1)
measure_time_heap_sort_reverse_sorted, _ = time_measure(heap_sort, heap_sort_reverse_table)
measure_time_selection_sort_reverse_sorted, _ = time_measure(selection_sort, selection_sort_reverse_table)

d = {
    "quick_sort": pd.Series(
        [measure_time_quick_sort_unsorted, measure_time_quick_sort_sorted, measure_time_quick_sort_reverse_sorted],
        index=["unsorted numbers sort time", "sorted numbers sort time", "reverse sorted numbers sort time"]),
    "heap_sort": pd.Series(
        [measure_time_heap_sort_unsorted, measure_time_heap_sort_sorted, measure_time_heap_sort_reverse_sorted],
        index=["unsorted numbers sort time", "sorted numbers sort time", "reverse sorted numbers sort time"]),
    "selection_sort": pd.Series(
        [measure_time_selection_sort_unsorted, measure_time_selection_sort_sorted, measure_time_selection_sort_reverse_sorted],
        index=["unsorted numbers sort time", "sorted numbers sort time", "reverse sorted numbers sort time"]),
}

quick_sort_sort_time = [measure_time_quick_sort_unsorted, measure_time_quick_sort_sorted, measure_time_quick_sort_reverse_sorted]
heap_sort_sort_time = [measure_time_heap_sort_unsorted, measure_time_heap_sort_sorted, measure_time_heap_sort_reverse_sorted]
selection_sort_sort_time = [measure_time_selection_sort_unsorted, measure_time_selection_sort_sorted, measure_time_selection_sort_reverse_sorted]

x = max(quick_sort_sort_time)
y = max(heap_sort_sort_time)
z = max(selection_sort_sort_time)



print(pd.DataFrame(d))

names = ['unsorted', 'sorted', 'reverse sorted ']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.scatter(names, quick_sort_sort_time)
plt.ylabel('time (s)')
plt.xlabel('quick sort')
plt.axis([-0.1,2.1, 0, x+0.2*x])
plt.subplot(132)
plt.scatter(names, heap_sort_sort_time)
plt.ylabel('time (s)')
plt.xlabel('heap sort')
plt.axis([-0.1,2.1, 0, y+0.2*y])
plt.subplot(133)
plt.scatter(names, selection_sort_sort_time)
plt.ylabel('time (s)')
plt.xlabel('selection sort')
plt.axis([-0.1,2.1, 0, z+0.2*z])

plt.suptitle('Sorted time')
plt.show()

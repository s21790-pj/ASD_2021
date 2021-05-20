import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sorting_functions_project.quicksort import quick_sort
from sorting_functions_project.heapsort import heap_sort
from sorting_functions_project.selection_sort import selection_sort
from sorting_functions_project.time_measure import time_measure

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

quick_sort_sort_time = []
heap_sort_sort_time = []
selection_sort_sort_time = []

for num in range(5):
    A_before_sort = []
    B_before_sort = []
    C_before_sort = []
    for num in range(10):
        x = random.randint(0, 10)
        A_before_sort.append(x)
        B_before_sort.append(x)
        C_before_sort.append(x)

    A_after_sort = A_before_sort.copy()
    B_after_sort = B_before_sort.copy()
    C_after_sort = C_before_sort.copy()

    A_table_to_time_measure = A_before_sort.copy()
    B_table_to_time_measure = B_before_sort.copy()
    C_table_to_time_measure = C_before_sort.copy()

    quick_sort_sorted_table = quick_sort(A_after_sort, 0, len(A_after_sort) - 1)
    heap_sort_sorted_table = heap_sort(B_after_sort)
    selection_sort_sorted_table = selection_sort(C_after_sort)

    quick_sort_start, quick_sort_end, quick_sort_time = \
        time_measure(quick_sort, A_table_to_time_measure, 0, len(A_table_to_time_measure) - 1)
    heap_sort_start, heap_sort_end, heap_sort_time = time_measure(heap_sort, B_table_to_time_measure)
    selection_sort_start, selection_sort_end, selection_sort_time = time_measure(selection_sort,
                                                                                 C_table_to_time_measure)

    d = {
        "quick_sort": pd.Series(
            [A_before_sort, quick_sort_sorted_table, quick_sort_start, quick_sort_end, quick_sort_time],
            index=["numbers", "sorted numbers", "start", "end", "sort time"]),
        "heap_sort": pd.Series([B_before_sort, heap_sort_sorted_table, heap_sort_start, heap_sort_end, heap_sort_time],
                               index=["numbers", "sorted numbers", "start", "end", "sort time"]),
        "selection_sort": pd.Series(
            [C_before_sort, selection_sort_sorted_table, selection_sort_start, selection_sort_end, selection_sort_time],
            index=["numbers", "sorted numbers", "start", "end", "sort time"]),
    }
    quick_sort_sort_time.append(quick_sort_time)
    heap_sort_sort_time.append(heap_sort_time)
    selection_sort_sort_time.append(selection_sort_time)
    print(pd.DataFrame(d))


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 0.0000010)

plt.plot(quick_sort_sort_time, label="quick_sort")
plt.plot(heap_sort_sort_time, label="heap_sort")
plt.plot(selection_sort_sort_time, label="selection_sort")
plt.ylabel("Time (s)")
plt.xlabel("Number of sort")
plt.legend()


plt.show()
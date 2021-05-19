from random import random
import timeit

from sorting_functions.quicksort import quick_sort
from sorting_functions.heapsort import heap_sort
from sorting_functions.selection_sort import selection_sort


A = [5, 2, 1, 12, 8, 13, 11, 9, 4, 2, 5, 7, 19, 3]


def time_measure(func):
    start = timeit.timeit()
    print(f"START: \n{start}")


time_measure(heap_sort(A))


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def partition(A, p, r):
    pivot = A[r]
    smaller = p
    for j in range(p, r):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller = smaller + 1
    A[smaller], A[r] = A[r], A[smaller]
    return smaller


# quick_sort(array, 0, len(array) - 1)
# print(array)
#
# def time_measure_quick_sort():
#     start = timeit.timeit()
#     print(f"START: \n{start}")
#     quick_sort(array, 0, len(array) - 1)
#     end = timeit.timeit()
#     print(f"END: \n{end}")
#     time_retsult = end - start
#     return time_retsult

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
    return A


def partition(A, p, r):
    pivot = A[r]
    smaller = p
    for j in range(p, r):
        if A[j] <= pivot:
            A[smaller], A[j] = A[j], A[smaller]
            smaller = smaller + 1
    A[smaller], A[r] = A[r], A[smaller]
    return smaller




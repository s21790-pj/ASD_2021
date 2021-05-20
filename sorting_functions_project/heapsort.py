def max_heapify(arr, arr_lengt, i):
    max_value = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < arr_lengt and arr[i] < arr[left]:
        max_value = left

    if right < arr_lengt and arr[max_value] < arr[right]:
        max_value = right

    if max_value != i:
        arr[i], arr[max_value] = arr[max_value], arr[i]
        max_heapify(arr, arr_lengt, max_value)


def build_max_heap(arr):
    heap_size = len(arr)
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(arr, heap_size, i)


def heap_sort(arr):
    build_max_heap(arr)
    heap_size = len(arr)
    for i in range(heap_size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)
    return arr


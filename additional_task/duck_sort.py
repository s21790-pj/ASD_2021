def duck_sort(arr):
    x = 0
    x_counter = 0
    y_counter = 0
    arr[0] = x
    for num in arr:
        if num == x:
            x_counter += 1
        else:
            y_counter += 1
    result = [x_counter, y_counter]
    return result





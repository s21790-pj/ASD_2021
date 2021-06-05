def duck_sort(arr):
    x_counter = 0
    y_counter = 0
    x = arr[0]
    result_arr = []
    for num in arr:
        if num == x:
            x_counter += 1
        else:
            y = num
            y_counter += 1
    if x > y:
        [result_arr.append(y) for _ in range(y_counter)]
        [result_arr.append(x) for _ in range(x_counter)]
    else:
        [result_arr.append(x) for _ in range(x_counter)]
        [result_arr.append(y) for _ in range(y_counter)]
    return result_arr


A = [1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1]

print(duck_sort(A))

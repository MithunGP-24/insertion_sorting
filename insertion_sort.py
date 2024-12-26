def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        # Place the key in its correct position
        arr[j + 1] = key

arr = [6, 4, 5, 2, 9, 1]
insertion_sort(arr)
print(arr)

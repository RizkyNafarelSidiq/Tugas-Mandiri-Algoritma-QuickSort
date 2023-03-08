def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# contoh penggunaan
arr = [3, 6, 2, 8, 1, 5, 7, 4]
sorted_arr = quicksort(arr)
print(sorted_arr)

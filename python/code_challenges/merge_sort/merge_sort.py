def merge_sort(input_array):
    n = len(input_array)
    if n <= 1:
        return
    else:
        mid = n/2
        i = 0
        left = []
        right = []
        for i in range(int(mid)):
            left.append(input_array[i])
        for i in range(int(mid),len(input_array)):
            right.append(input_array[i])
        merge_sort(left)
        merge_sort(right)
        merge(left,right,input_array)
    return input_array

def merge(left_array, right_array, combined_sorted):    
    n_l = len(left_array)
    n_r = len(right_array)
    i = 0
    j = 0
    k = 0
    while i < n_l and j < n_r:
        if left_array[i] <= right_array[j]:
            combined_sorted[k] = left_array[i]
            i += 1
        else:
            combined_sorted[k] = right_array[j]
            j += 1
        k += 1
    while i < n_l:
        combined_sorted[k] = left_array[i]
        i += 1
        k += 1
    while j < n_r:
        combined_sorted[k] = right_array[j]
        j += 1
        k += 1

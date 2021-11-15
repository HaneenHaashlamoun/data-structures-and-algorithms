# Merge Sort 
merge sort and is based on a divide and conquer approach
merge sort is an efficient, general-purpose, and comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output.

![merge](https://i.imgur.com/HU2tfzo.gif)

to analyze any array :
[**Try this**](https://www.101computing.net/wp/wp-content/uploads/merge-sort.html)

example: 

![mergesort](https://www.101computing.net/wp/wp-content/uploads/Merge-Sort-Algorithm.png)
*[source](https://www.101computing.net/merge-sort-algorithm/)*

## Pseudo Code
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```


## Efficiency:
Merge Sort is a stable sort which means that the same element in an array maintain their original positions with respect to each other. Overall time complexity of Merge sort is O(nLogn). It is more efficient as it is in worst case also the runtime is O(nlogn) The space complexity of Merge sort is O(n).



## Code 
```
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
```

## Whiteboard Process

![mergesort](merge_sort.jpg)
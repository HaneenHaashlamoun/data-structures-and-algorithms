# Quick Sort

It works by dynamically swapping elements within the list around a selected pivot, and by then recursively sorting the sub-lists to either side of this pivot. This makes it significantly more space-efficient, which can be important for huge lists.
Quicksort depends on two key factors — selecting the pivot and the mechanism for partitioning the elements.

The key to this algorithm is the partition function, which we’ll cover soon. This returns an index into the input array such that every element below this index sorts as less than the element at this index, and the element at this index sorts as less than all the elements above it.

Doing this will involve swapping some of the elements in the array around so that they are the appropriate side of this index.

Once we’ve done this partitioning, we then apply the algorithm to the two partitions on either side of this index. This eventually finishes when we have partitions that contain only one element each, at which point the input array is now sorted.

As a result, we can summarize the quick sort algorithm with three steps:

- Pick an element as a pivot
- Partition the problem set by moving smaller elements to the left of the pivot and larger elements to its right
- Repeat the above steps on each partition


![qs](https://www.baeldung.com/wp-content/uploads/sites/4/2020/07/final-2.png)
*[source](https://www.baeldung.com/cs/algorithm-quicksort)*


## Pseudo Code

```
ALGORITHM QuickSort(arr, left, right)
 if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

![qs](https://www.tutorialspoint.com/data_structures_algorithms/images/quick_sort_partition_animation.gif?w=144)

## Code

```
def quick_sort(list, left, right):

    if left < right:
        position = partition(list, left, right)
        quick_sort(list, left, position-1)
        quick_sort(list, position + 1, right)
    return list


def partition(list, left, right):
    pivot = list[right]
    low = left - 1
    for i in range(left, right):
        if list[i] <= pivot:
            low += 1
            swap(list, i, low)
    swap(list, right, low + 1)
    return low + 1


def swap(list, i, low):
    temp = list[i]
    list[i] = list[low]
    list[low] = temp


arr = [8, 4, 23, 42, 16, 15]
print('before',arr)
print('after',quick_sort(arr, 0, len(arr)-1))

```

## Quick Sort test

```
def test_quick_sort():
    list = [8, 4, 23, 42, 16, 15]
    actual = quick_sort(list, 0, len(list)-1)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected
```

myArr = [-131, -82, 0, 27, 42, 68, 179]
value = 42

def BinarySearch(allArr, searchVal):
    high = len(allArr) - 1
    low = 0
    while low <= high:
        mid = (low+high) // 2
        if allArr[mid] == searchVal:
            return mid
        if allArr[mid] < searchVal:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(BinarySearch(myArr, value))

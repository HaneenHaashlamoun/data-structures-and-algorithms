def selection_sort(arr:list[int]) :    
    for i in range(len(arr)):
        min = arr[i]
        min_idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_idx = j      
        if not min_idx == i:
            temp = arr[i]
            arr[i] = min
            arr[min_idx]= temp
    return arr

# thelist = [8,4,23,42,16,15]
# print(selection_sort(thelist))

##### Pseudo Code ######
# SelectionSort(int[] arr)
#     DECLARE n <-- arr.Length;
#     FOR i = 0; i to n - 1  
#         DECLARE min <-- i;
#         FOR j = i + 1 to n
#             if (arr[j] < arr[min])
#                 min <-- j;
#         if (arr[j] < arr[min]):   // ADDED ON THE ORIGINAL Pseudo Code
#         DECLARE temp <-- arr[min];
#         arr[min] <-- arr[i];
#         arr[i] <-- temp;
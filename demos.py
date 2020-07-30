def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        num = arr[-1]
        for x in arr:
            less_than, equal, more_than = [],[],[]
            if x < num:
                less_than.append(x)
            elif x == num:
                equal.append(x)
            else: 
                more_than.append(x)
    return quicksort(less_than) + equal + quicksort(more_than)

def merge_sorted(arr1,arr2):
    sorted_arr = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i  < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr

def mergesort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = mergesort(arr[:middle])
        l2 = mergesort(arr[middle:])
        return merge_sorted(l1,l2)

def bubblesort(arr):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arr)-1):
            if arr[num] > arr[num+1]:
                swap_happened = True
                arr[num], arr[num+1] = arr[num+1], arr[num]


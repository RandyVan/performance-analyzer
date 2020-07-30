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


l = [2,3,6,3,76,34,2,0,54,3,12,1,43]
quicksort(l)
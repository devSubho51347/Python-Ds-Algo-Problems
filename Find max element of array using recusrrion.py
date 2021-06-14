def getMax(low,high,arr):
    ## If only one element is present in array
    if low == high:
        arr_max = arr[low]
        return arr_max
    # If only two elements are present

    elif high == low + 1:
        arr_max = max(arr[low],arr[high])
        return arr_max

    else:
        mid = (low + high) // 2
        arr_max_left = getMax(low,mid,arr)
        arr_max_right = getMax(mid,high,arr)
        return max(arr_max_left,arr_max_right)

arr = [int(x) for x in input().split()]
print("Max element is:", getMax(0,len(arr) - 1,arr))

def cyclially_rotate(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr

    else:
        for i in range(0,len(arr)-1,1):
            arr[len(arr) - 1-i], arr[len(arr) - 2 - i] = arr[len(arr) - 2 - i],  arr[len(arr) - 1-i]
        return arr


li = [int(x) for x in input().split()]

print("Cyclially rotated array is:", cyclially_rotate(li))


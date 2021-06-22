# VERSION 1

def shift_negative(arr):
    ## defining two pointers n1 and n2

    n1 = 0
    n2 = 0
    while n2 < len(arr):
        if arr[n2] < 0:
            if n1 != n2:
               arr[n1], arr[n2] = arr[n2], arr[n1]
            n1 += 1
            n2 += 1
        else:
            n2 += 1


    return arr

li = [int(x) for x in input().split()]
print(shift_negative(li))



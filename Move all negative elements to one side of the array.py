# VERSION 1
# Better approach is version 1
def shift_negative_method1(arr):
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

# Version 2

#Implementation using stack

def shift_negative_method2(arr):
    li = []
    i = 0
    while i < len(arr):
        if len(li) == 0 and arr[i] > 0:
            li.append(i)
            i = i + 1
        elif arr[i] < 0:
            if len(li) == 0:
                i = i +1
            else:
                arr[i],arr[li[0]] = arr[li[0]],arr[i]
                li.pop(0)
                li.append(i)
                i = i + 1
        else:
            li.append(i)
            i = i + 1
    print(*arr)


li = [int(x) for x in input().split()]
shift_negative_method2(li)


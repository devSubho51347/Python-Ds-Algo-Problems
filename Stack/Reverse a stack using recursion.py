def reverse_stack(arr):
    if len(arr) == 1:
        return arr
    li = []
    for i in range(1,len(arr),1):
        li.append(arr.pop())

    top_ele = arr.pop()
    for i in range(0,len(li),1):
        arr.append(li.pop())

    reversed_array = reverse_stack(arr)
    reversed_array.append(top_ele)

    return reversed_array

arr = [int(x) for x in input().split()]
print(*reverse_stack(arr))
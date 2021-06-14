def reverse_array(array,start, end):
    if start >= end:
        return array
    array = reverse_array(array,start = start + 1, end = end - 1)
    array[start], array[end] = array[end],array[start]
    return array





array = [int(x) for x in input().split()]
l = len(array)

print(reverse_array(array,0,l - 1))

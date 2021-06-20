# Version 1

def reverse_array(array,start, end):
    if start >= end:
        return

    array[start], array[end] = array[end],array[start]
    reverse_array(array,start = start + 1, end = end - 1)





array = [int(x) for x in input().split()]
l = len(array)
print(array)
reverse_array(array,0,l - 1)
print("reversed array:", array)



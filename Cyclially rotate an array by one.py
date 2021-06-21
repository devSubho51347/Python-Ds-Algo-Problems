# Version 1
# Space complexity O(1) And Time Complexity O(n)

# def cyclially_rotate(arr):
#     if len(arr) == 0:
#         return None
#     elif len(arr) == 1:
#         return arr
#
#     else:
#         for i in range(0,len(arr)-1,1):
#             arr[len(arr) - 1-i], arr[len(arr) - 2 - i] = arr[len(arr) - 2 - i],  arr[len(arr) - 1-i]
#         return arr
#
#
# li = [int(x) for x in input().split()]
#
# print("Cyclially rotated array is:", cyclially_rotate(li))

# Version 2
# Using recursive approach

def reverse(arr,i):
    if i == len(arr) - 1:
        return arr
    print(arr)

    reverse(arr,i + 1)
    arr[i+1],arr[i] = arr[i],arr[i+1]
    print(arr)
    return arr

li = [int(x) for x in input().split()]
print(reverse(li,0))

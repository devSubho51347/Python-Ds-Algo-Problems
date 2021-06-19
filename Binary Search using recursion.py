# APPROACH 1 using iterative approach


# def binary_search(arr,n):
#     if len(arr) == 0:
#         return False
#     # si means start index
#     # ei means end index
#     # mid = si + ei // 2
#     si = 0
#     ei = len(arr) - 1
#
#     while si <= ei:
#       mid = (si + ei) // 2
#       if arr[mid] == n:
#           print("True")
#           return
#
#
#       elif arr[mid] > n:
#         ei = mid - 1
#       elif arr[mid] < n:
#         si = mid + 1
#
#
# li = [int(x) for x in input().split()]
# n = int(input())
# print("Is n preent in array:", binary_search(li,n))


# APPROACH using recursive approach

def binary_search(arr,n,si,ei):
    if si > ei:
        return False
    mid = (si + ei) // 2
    if arr[mid] == n:
        return mid
    elif arr[mid] > n:
        return binary_search(arr,n,si,mid - 1)
    elif arr[mid] < n:
        return binary_search(arr,n,mid + 1,ei)

arr = [int(x) for x in input().split()]
n = int(input())
print("Requiered index of {} is :".format(n), binary_search(arr,n,0,len(arr) - 1))
if binary_search(arr,n,0,len(arr) - 1) is False:
    print("Required element is not present in the given list")
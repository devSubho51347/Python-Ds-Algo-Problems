# si means start index
# n is the required no whose index we need to search
def first_index(arr,si,n):
    if len(arr) == si + 1:
        if arr[si] == n:
            return si
        else:
            return -1

    if arr[si] == n:
        return si
    else:
        return first_index(arr,si + 1,n)

li = [int(x) for x in input().split()]
n = int(input())
print("The first index of our required no {} is:".format(n), first_index(li,0,n))
if first_index(li,0,n) == -1:
    print("Required no is not present in the given array")
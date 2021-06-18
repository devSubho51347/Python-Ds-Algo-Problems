# si = start index
# ri = required index
# n is no to be found
def last_index(arr,si,ri,n):
    if len(arr) == si + 1:
        if arr[si] == n:
            return si
        else:
            return ri

    if arr[si] == n:
        ri = si
    return last_index(arr,si+1,ri,n)


li = [int(x) for x in input().split()]
n = int(input())
print("Last index of required no {} is:".format(n), last_index(li,0,-1,n))

if last_index(li,0,1,n) == -1:
    print("The no is not present in the given array")

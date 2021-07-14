def find_max(arr, n, k):
    arr.sort()
    count = 0
    i = 0
    sum = 0
    while count <=k and i < n:
        if sum == 0:
            sum = arr[n - i -1]
            count = count + 1
        elif arr[n - i -1] == arr[n - i]:
            sum = sum + arr[n - i - 1]
        else:
            count = count + 1
            if count <= k:
               sum = sum + arr[n - i - 1]
        i = i + 1
    print(sum)

t = int(input())
i = 0
while i < t:
    n, k = input().split(" ")
    arr = [int(x) for x in input().split()]
    find_max(arr, int(n), int(k))

    i = i + 1
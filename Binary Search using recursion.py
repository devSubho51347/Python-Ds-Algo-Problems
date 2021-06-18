def binary_search(arr,n):
    if len(arr) == 0:
        return False
    # si means start index
    # ei means end index
    # mid = si + ei // 2
    si = 0
    ei = len(arr) - 1

    while si <= ei:
      mid = (si + ei) // 2
      if arr[mid] == n:
          print("True")
          return


      elif arr[mid] > n:
        ei = mid - 1
      elif arr[mid] < n:
        si = mid + 1


li = [int(x) for x in input().split()]
n = int(input())
print("Is n preent in array:", binary_search(li,n))

# Version 1 when all the elements in the array are distinct

# def find_union(arr1,arr2):
#     # n1 = len(arr1)
#     # n2 = len(arr2)
#     s1 = 0
#     s2 = 0
#     e1 = 0
#     e2 = 0
#     arr = []
#
#     while s1 < len(arr1) and s2 < len(arr2):
#         if arr1[s1] == arr2[s2]:
#             arr.append(arr1[s1])
#             e1 += 1
#             e2 += 1
#
#
#         elif arr1[s1] > arr2[s2]:
#
#             while e2 < len(arr2) and (arr1[s1] >= arr2[e2]):
#                 e2 += 1
#             for ele in arr2[s2:e2:1]:
#                 arr.append(ele)
#             if arr[-1] != arr1[s1]:
#                 arr.append(arr1[s1])
#             e1 += 1
#
#         elif arr1[s1] < arr2[s2]:
#
#             while e1 < len(arr1) and (arr1[e1] <= arr2[s2]):
#                 e1 += 1
#             for ele in arr1[s1:e1:1]:
#                 arr.append(ele)
#             if arr[-1] != arr2[s2]:
#                 arr.append(arr2[s2])
#
#             e2 += 1
#
#         s1 = e1
#         s2 = e2
#
#
#
#
#
#     while e1 < len(arr1):
#
#         arr.append(arr1[e1])
#         e1 += 1
#
#     while e2 < len(arr2):
#         arr.append(arr2[e2])
#         e2 += 1
#
#     return arr
#
#
#
#
#
#
# arr1 = [int(x) for x in input().split()]
# arr2 = [int(x) for x in input().split()]
#
# print("Union of the two given arrays is:", find_union(arr1,arr2))


# Version 2 when all the elements in the array are not distinct

def doUnion(arr1,arr2):
    # n1 = len(arr1)
    # n2 = len(arr2)

    arr1 = list(set(arr1))
    arr2 = list(set(arr2))
    arr1.sort()
    arr2.sort()
    s1 = 0
    s2 = 0
    e1 = 0
    e2 = 0
    arr = []

    while s1 < len(arr1) and s2 < len(arr2):
        if arr1[s1] == arr2[s2]:
            arr.append(arr1[s1])
            e1 += 1
            e2 += 1


        elif arr1[s1] > arr2[s2]:

            while e2 < len(arr2) and (arr1[s1] >= arr2[e2]):
                e2 += 1
            for i in range(s2, e2, 1):
                if len(arr) == 0:
                    arr.append(arr2[i])
                elif arr[-1] != arr2[i]:
                    arr.append(arr2[i])

            if arr[-1] != arr1[s1]:
                arr.append(arr1[s1])
            e1 += 1

        elif arr1[s1] < arr2[s2]:

            while e1 < len(arr1) and (arr1[e1] <= arr2[s2]):
                e1 += 1
            for i in range(s1, e1, 1):
                if len(arr) == 0:
                    arr.append(arr1[i])
                elif arr[-1] != arr1[i]:
                    arr.append(arr1[i])
            if arr[-1] != arr2[s2]:
                arr.append(arr2[s2])

            e2 += 1

        s1 = e1
        s2 = e2

    while e1 < len(arr1):
        arr.append(arr1[e1])
        e1 += 1

    while e2 < len(arr2):
        arr.append(arr2[e2])
        e2 += 1

    return arr

arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

print("Union is:", doUnion(arr1,arr2))
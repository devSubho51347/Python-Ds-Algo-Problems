# The commented out solution is wrong

# def count_and_say(n):
#     if n == 1:
#         return "1"
#     if n == 2:
#         return "11"
#     str_data = count_and_say(n-1)
#     str1 = ""
#
#     dict = {}
#
#     for i in range(0,len(str_data),1):
#         if i == 0:
#             dict[str_data[i]] = dict.get(str_data[i], 1)
#
#         elif str_data[i] == str_data[i-1]:
#
#               dict[str_data[i]] = dict.get(str_data[i],1) + 1
#
#
#
#
#
#
#         else:
#
#
#
#               dict[str_data[i]] = dict.get(str_data[i], 1)
#     i = 0
#     while i < len(str_data):
#         str1 = str1 + str(dict[str_data[i]]) + str_data[i]
#         i = i + dict[str_data[i]]
#     return str1

# correct solution is in below
# recursive approach
def count_and_say(n):
    if n == 1:
        return "1"
    if n == 2:
        return "11"
    str_data = count_and_say(n - 1)

    str2 = ""

    count = 0
    for i in range(0, len(str_data), 1):
        if i == 0:
           count = count + 1
        elif str_data[i] == str_data[i - 1]:
            if i != len(str_data) - 1:
                count = count + 1
            else:
                count = count + 1
                str2 = str2 + str(count) + str_data[i]
        else:
            if i != len(str_data) - 1:
                str2 = str2 + str(count) + str_data[i - 1]
                count = 1

            else:
                str2 = str2 + str(count) + str_data[i - 1]
                count = 1
                str2 = str2 + str(count) + str_data[i]

    return str2


n = int(input())
print(count_and_say(n))

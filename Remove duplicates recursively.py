# Approach 1
#
# def remove_duplicates(str,char):
#     if len(str) == 0:
#         return ""
#     # if char == "":
#     #     str[0] = char
#     if str[0] == char:
#         return remove_duplicates(str[1::],char)
#     elif str[0] != char:
#         char = str[0]
#         str = str[0] + remove_duplicates(str[1::],char)
#         return str
#
# str = input()
# print("Final string is:", remove_duplicates(str,""))


# Approach 2

def remove_duplicates(str):
    if len(str) == 1:
        return str

    str2 = remove_duplicates(str[1::])

    if str[0] == str[1]:
        return str2
    else:
        str2 = str[0] + str2
        return str2



str = input()
print("Final string is:", remove_duplicates(str))



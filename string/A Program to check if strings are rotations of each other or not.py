def areRotation(str1,str2):
    str3 = ""
    j = 0
    for i in range(0,len(str1),1):
        if str2[j] == str1[i]:
            j = j + 1
        elif j == 0:
            str3 = str3 + str1[i]
        else:
            return False
    if str2[j:len(str2):1] == str3:
        return True
    else:
        return False



str1 = input()
str2 = input()
print(areRotation(str1,str2))
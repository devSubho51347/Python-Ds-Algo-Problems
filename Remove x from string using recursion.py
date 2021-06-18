def remove_x(str):
    if len(str) == 0:
        return ""
    if str[0] == 'x' and len(str) != 1:
        str = str[1::]
        return remove_x(str)
    elif str[0] == 'x' and len(str) == 1:
        return ""
    else:
        str = str[0] + remove_x(str[1::])
    return str

string = input()
print(remove_x(string))
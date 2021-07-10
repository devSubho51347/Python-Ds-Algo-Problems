def minimum_bracket_reversal(str):
    i = 0
    count = 0
    li = []
    j = 0
    l = len(str)

    if (l % 2) == 0:
        while i < l:
            if i == 0:
                li.append(str[i])
            elif str[i] == "}" and li[-1] == "{":
                li.pop()

            else:
                li.append(str[i])
            i = i + 1

        while j < len(li):
            if li[j] == "}" and li[j + 1] == "{":
                count += 2
            elif li[j] == "}" and li[j + 1] == "}":
                count = count + 1
            elif li[j] == "{" and li[j + 1] == "{":
                count = count + 1
            j = j + 2

    else:
        return -1
    return count


str = input()
print(minimum_bracket_reversal(str))
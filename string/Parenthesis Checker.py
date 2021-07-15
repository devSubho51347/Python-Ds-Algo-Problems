def ispar(s):
    # code here
    li = []
    for ele in s:
        if ele in ["{", "(", "["]:
            li.append(ele)
        elif ele in ["}", ")", "]"] and len(li) != 0:
            if ele == ")" and li[-1] == "(":
                li.pop()
            elif ele == "}" and li[-1] == "{":
                li.pop()
            elif ele == "]" and li[-1] == "[":
                li.pop()
            else:
                return False
        else:
            return False
    if len(li) == 0:
        return True
    else:
        return False


str = input()
if ispar(str):
    print("Balanced")
else:
    print("Not Balanced")
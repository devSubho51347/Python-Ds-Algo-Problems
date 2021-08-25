str = input()
dict = {}
for ele in str:
    dict[ele] = dict.get(ele,0) + 1
for ele in dict:
    if dict[ele] > 1:
        print(ele,"count:{}".format(dict[ele]))

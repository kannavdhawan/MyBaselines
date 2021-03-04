def func(list_string):
    dic = {}
    for i in list_string:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] +=1
    return dic

print(func(['a','b','c','a','b']))


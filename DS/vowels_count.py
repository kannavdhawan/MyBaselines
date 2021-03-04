def count(str):
    list_v = ['a','e','i','o','u']
    c = {'cons':0,'vow':0}
    for i in str:
        if i in list_v:
            c['cons']+=1
        else:
            c['vow']+=1
    return c

print(count('abcdefghijklmnopqrstuvwxyz'))

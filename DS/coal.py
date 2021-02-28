def minJumps(arr, h):
    unblock = '.'
    block = '#'

    # len check case
    len_set = {}
    for i in arr:
        len_set.add(len(i))
    if len(len_set) != 1:
        return 'No'

    c = 0
    for i in arr:
        for j in i:
                

print('Minimum number of jumps to reach',
      'end is', minJumps(['..', '..'], 3))


##  ..
##  ..

def seq_search(arr,ele):
    # unordered
    i = 0
    found = False

    while i < len(arr) and not found:
        if arr[i] == ele:
            return True
        else:
            i += 1

    return found

print(seq_search([1,2,3,4],5))

def ordered_search(arr,ele):
    i = 0
    stop = False
    while i < len(arr) : # and not stop
        if arr[i] == ele:
            return True
        else:
            if arr[i] > ele:
                return False
                # stop = True
            i += 1
    return False
print(ordered_search([1,2,3,4],0))
















def search(arr,ele):
    if ele in arr:
        return True
    else:
        return False

print(search([1,2,3,4,5],4))
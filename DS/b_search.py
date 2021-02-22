def b_search(arr, ele):

    sorted_arr = sorted(arr)
    start = 0
    end = len(arr) - 1
    found = False

    while not found and start <= end:
        mid = (start+end)//2
        if sorted_arr[mid] == ele:
            found = True
        elif sorted_arr[mid] > ele:
            end = mid - 1
        else:
            start = mid + 1

    return mid

loc = b_search([1, 2, 5, 6], 2)
print("Found at {}".format(loc))
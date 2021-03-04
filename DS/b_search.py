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


arr = [1,2,3,4,5,6,7]

def func(arr,ele):
    low = 0
    high = len(arr) - 1
    # ele = 5
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == ele:
            return mid
        elif ele > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return "Not Found"
print(func(arr, 5))



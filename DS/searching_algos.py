# Lineara search

def linear(arr,ele):
    i = 0
    while i < len(arr):
        if arr[i] == ele:
            return i
        else:
            i = i+1

    return "Not Found"

print(linear([1,2,3,4],3))

def binary(arr,ele):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)//2
        if arr[mid] == ele:
            return mid
        elif ele < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "Not Found"

print(binary([1,2,3,4,5,6],4))


# Bubble

def bubble_sort(arr):
    for n in range(len(arr)-1, 0, -1):
        for k in range(n):
            if arr[k] > arr[k+1]:
                tmp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = tmp

            else:
                continue
    return arr

arr = [3,2,13,4,6,5,7,8,1,20]
print(bubble_sort(arr))


def selection_sort(arr):

    for i in range(0,len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                temp = arr[j]
                arr[j] = arr[min_idx]
                arr[min_idx] = temp

    return arr
arr = [3,2,13,4,6,5,7,8,1,20]
print(selection_sort(arr))

def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i] < arr[j]:
                arr.insert(j, arr[i])
                arr.pop(i+1)
    return arr

# arr = [12, 11, 13, 5, 6]

print(insertion_sort(arr))
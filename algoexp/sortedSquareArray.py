# Write a function that takes in a non-empty array of integers that are sorted in ascending order at
# sorted in ascending order.

def sortedSquaredArray(array):
    # Write your code here.
    resultantArray = [0 for _ in array]
    # resultantArray = []
    for idx in range(len(array)):
        resultantArray[idx] = array[idx] * array[idx]
    # resultantArray.append(array[idx]*array[idx])
    return sorted(resultantArray)


print(sortedSquaredArray([1, 2]))
print(sortedSquaredArray([-2, 1]))

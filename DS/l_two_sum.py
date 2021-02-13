# For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7
# and 2 + 5 = 7.
def two_number_sum(array, target_sum):
    x = []
    final = []
    for i in array:
        x.append(target_sum - i)
    print(x)
    for i in range(0, len(array)):
        temp = array.pop(0)
        if x[i] in array:
            final.extend([[temp, x[i]]])
    return final

if __name__ == '__main__':
    print(two_number_sum([3, 5, 2, -4, 8, 11], 7))

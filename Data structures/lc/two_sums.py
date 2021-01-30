# For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7, your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.

def two_number_sum(array,target_sum):
    final_list=[]
    for n in array:

        residual = target_sum - n
        if residual in array and residual != n:
            final_list.append([n,residual])
            array.remove(n)
    return final_list


if __name__=='__main__':
    print(two_number_sum([3, 5, -4, 8, 11, 1, -1, 6], 10))

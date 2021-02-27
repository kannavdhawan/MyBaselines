# Given an array of arrays where each sub-array contains an arbitrary number of random strings, find the strings that
# occur in every sub-array and return them (the returned result strings must also be in an array).
# There can be duplicates of the same string in any of the sub-arrays.
def common_strings(arr):

    final = []
    for i in set(arr[0]):
        c = 0
        for j in range(1,len(arr)):
            if i in arr[j]:
                c+=1
            if c == len(arr) -1:
                final.append(i)
    return final

arr = [['kannav', 'T','D', 'kannav'],['kannav','Dhawan','T','K'],['kannav','T','D']]
cs = common_strings(arr)
print(cs)


# def common_strings(arr):
#
#   if len(arr)==0:
#     return None
#   arr1=arr[0]
#   In_all_arrays=[]
#   for val in arr1:
#     count=0
#     for j in range(1,len(arr)):
#       if val not in arr[j]:
#         break;
#       if val in arr[j]:
#         count+=1
#     if count==(len(arr)-1):
#       In_all_arrays.append(val)
#   return In_all_arrays

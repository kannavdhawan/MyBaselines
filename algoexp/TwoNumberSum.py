# Write a function that takes in a non-empty array of distinct integers and an integer representing a
# target sum. If any two numbers in the input array sum up to the target sum, the function should
# return them in an array, in any order. If no two numbers sum up to the target sum, the function
# should return an empty array.
# Note that the target sum has to be obtained by summing two different integers in the array; you
# can't add a single integer to itself in order to obtain the target sum.
# You can assume that there will be at most one pair of numbers summing up to the target sum.
# Sample Input
# array
# =13, 5,
# targetSum = 10
# -4, 8,

def twoNumberSum(array, targetSum):
	# Write your code here.
	for i in range(0, len(array)):
		j = targetSum - array[i]
		# temp = array.pop(i)
		if j in array[i+1:]:
			return [array[i], j]
	return []


print(twoNumberSum([13, 5, 3, 4, 7], 10))

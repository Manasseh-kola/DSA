"""
Write a function that takes in a sorted array of integers as well as a target integer. The function should use the Binary Search
algorithm to determine if the target integer is contained in the array and should return its index if it is, otherwise -1 .

Sample Input
array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
target = 33

Sample Output
3

"""

def binarySearch(array, target):
    return searchHelper(0,len(array)-1,array,target)
	
def searchHelper(L,R,array,target):
	if L>R:
		return -1
	rootNode = (L+R) // 2
	if array[rootNode ]== target:
		return rootNode
	elif array[rootNode] > target:
		return searchHelper(L,rootNode-1,array,target)
	else:
		return searchHelper( rootNode+1,R,array,target)
	

import math
def solution(array,start,end):
    n = len(array)
    #Array must be a power of 2.(To ensure the tree is full)
    #Extra zeros are added to the array if its not a power of 2.
    balance = 2**(math.ceil(math.log2(n))) - 2**(n)
    for _ in range(balance):
        array.append(0)

    #Length of segment Tree = 2 x len(array)
    #All parents are initiated to zero
    #Note the tree is 1-indexed i.e first index is 1
    segmentTree = [0 for _ in range(len(array))]
    for num in array:
        segmentTree.append(num)

    #Calculating parents
    #Left Child = 2*index. Right Child = 2*index+1
    #Parent = left Child + Right Child
    i = len(array)-1
    while i >=1:
        segmentTree[i] = segmentTree[2*i] + segmentTree[2*i+1]
        i-=1

    #Left child's index is even
    #Right child's index is odd
    # If left pointer "a" is on a right child add value at a to runningSum and increment a
    # If right pointer "b" is on a a left child add value at b to runningSum and incremnt b
    def rangeSum(a,b):
        a +=n; b+=n
        currSum = 0
        while a<=b:
            if a%2 ==1:
                currSum += segmentTree[a]
                a+=1
            if b%2 == 0:
                currSum += segmentTree[b]
                b-=1
            #Parent of index i = i//2
            a //=2; b //=2
        return currSum

    return rangeSum(start,end)

array = [5,8,6,3,2,7,2,6]
result = solution(array,2,7)
print(result)
    




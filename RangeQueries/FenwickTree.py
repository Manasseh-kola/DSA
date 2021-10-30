"""
FenwickTree for sum queries and value updates.
"""
#Function to update fenwick tree 
def solution(input,a,b):
    def updateTree(k,num):
        while k< len(input)+1:
            fenwickTree[k] +=num
            k +=k&(-k)
    # Construct Fenwick tree O(nlog(n))
    fenwickTree = [0 for i in range(1+len(input))]
    for i,num in enumerate(input):
        k = i+1
        updateTree(k,num)

    def getRangeSum(start,end):
        k = end+1
        currentSum = 0
        while k > start:
            currentSum += fenwickTree[k]
            k -= k&(-k)
        return currentSum

    return getRangeSum(0,b) - getRangeSum(0,a-1)

input = [3,2,-1,6,5,4,-3,3,7,2,3]
result = solution(input,3,8)
print(result)

    



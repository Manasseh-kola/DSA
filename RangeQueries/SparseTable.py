"""
Sparse Table for min queries
"""
import math
def solution(input,a,b):
    sparseTable = [[i] for i in range(len(input))]
    j = 1
    while 2**j <= len(input):
        i = 0 
        while i+2**(j)-1 < len(input):
            if input[sparseTable[i][j-1]] < input[sparseTable[i+2**(j-1)][j-1]]:
                sparseTable[i].append(sparseTable[i][j-1])
            else:
                sparseTable[i].append(sparseTable[i+2**(j-1)][j-1])
            
            i +=1
        j+=1


    def minRange(start,end):
        length = end-start+1
        k = math.floor(math.log2(length)) # k is the largest power of two that does not exceed end-start+1(length)(range)
        minValue = min(input[sparseTable[start][k]],input[sparseTable[start+(length-2**k)][k]])
        return minValue

    return minRange(a,b)

input = [1,3,4,8,6,1,4,2]
result = solution(input,1,4)
print(result)

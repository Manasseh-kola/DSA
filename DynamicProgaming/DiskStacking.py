"""
You're given a non-empty array of arrays where each subarray holds three integers and represents a disk. These integers denote each
disk's width, depth, and height, respectively. Your goal is to stack up the disks and to maximize the total height of the stack. A disk
must have a strictly smaller width, depth, and height than any other disk below it.
Write a function that returns an array of the disks in the final stack, starting with the top disk and ending with the bottom disk. Note
that you can't rotate disks; in other words, the integers in each subarray must represent [width, depth, height] at all times. You can assume that there will only be one
stack with the greatest total height.

Sample Input
disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2,3,4], [1,3,1], [4,4,5]]
Sample Output
[[2, 1, 2], [3, 2, 3], [4, 4, 5]]

"""

def diskStacking(disks):
    # Write your code here
    disks.sort(key=lambda x:x[2],reverse=True)
    return dfs(-1,None,0,len(disks),0,disks,{})[1]
	
def dfs(index,root,start,end,height,disks,memo):
    if index in memo:
      return memo[index]

    childHeight = 0
    maxChild = []
    for i in range(start,end):
      child = disks[i]
      if root is None or (child[0] < root[0] and child[1] < root[1] and child[2]< root[2] ):
        child = dfs(i,child,i+1,end,child[2],disks,memo)
        if child[0] > childHeight:
          childHeight = child[0]
          maxChild = child[1]
          
    if root is not None:
      maxChild.append(root)
    maxHeight = childHeight + height
    memo[index] = (maxHeight,maxChild)
    return (maxHeight,maxChild)

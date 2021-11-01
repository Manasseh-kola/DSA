"""
107. Binary Tree Level Order Traversal II
Medium
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        queue = deque([(root,0)])
        levels = set()
        bottomUp = []
        
        while len(queue):
            
            currentNode,currentLevel = queue.popleft()
            
            if currentNode is None:
                continue
                
            if currentLevel not in levels:
                bottomUp.append([])
                
            levels.add(currentLevel)
            bottomUp[currentLevel].append(currentNode.val)
            
            queue.append((currentNode.left,currentLevel+1))
            queue.append((currentNode.right,currentLevel+1))
            
        
        return bottomUp[::-1]
        

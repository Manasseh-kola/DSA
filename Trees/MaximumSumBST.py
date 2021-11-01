"""
1373. Maximum Sum BST in Binary Tree
Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = 0
             
    def maxSumBST(self, root: TreeNode) -> int:
        self.validateBST(root)
                
        if not root: return 0
        return self.maxSum
        
    
    def validateBST(self,tree):
        if tree is None:
            return {"valid": True,"nodeSum":0,"minVal":None,"maxVal":None}
        
        
        leftInfo = self.validateBST(tree.left)
        rightInfo = self.validateBST(tree.right)
        
        leftSum,rightSum = leftInfo["nodeSum"],rightInfo["nodeSum"]
        leftValid,minLeft,maxLeft = leftInfo["valid"],leftInfo["minVal"],leftInfo["maxVal"]
        minRight,maxRight=rightInfo["minVal"],rightInfo["maxVal"]
        rightValid = rightInfo["valid"]
        
        nodeSum = leftSum + rightSum
        currentValid = True
        minVal = None
        maxVal = None
        
        if not leftValid or not rightValid:
             return {"valid": False,"nodeSum":0,"minVal":None,"maxVal":None}
        
        
        if maxLeft is None and maxRight is None and minRight is None and minLeft is None:
            minVal = tree.val
            maxVal = tree.val
            nodeSum += tree.val
            
        elif minRight is None and maxRight is None:
            if tree.val <= maxLeft:
                currentValid = False
            else:
                nodeSum +=tree.val
            
            minVal = min(tree.val,minLeft)
            maxVal = max(tree.val,minLeft)
        
        elif minLeft is None and maxLeft is None:
            if tree.val >= minRight:
                currentValid = False
            else:
                nodeSum += tree.val
                
            minVal = min(tree.val,minRight)
            maxVal = min(tree.val,maxRight)
        else:
            if tree.val <= maxLeft or tree.val >= minRight:
                currentValid = False
            else:
                nodeSum += tree.val
                
            minVal = min(tree.val,minLeft,minRight)
            maxVal = max(tree.val,maxLeft,maxRight)
            
        valid = currentValid and leftValid and rightValid
        
        if valid:
            self.maxSum = max(self.maxSum,nodeSum)
        return {"valid":valid,"nodeSum":nodeSum,"minVal":minVal,"maxVal":maxVal}

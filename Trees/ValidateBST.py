"""
98. Validate Binary Search Tree
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root,float("-inf"),float("+inf"))
        
    def validate(self,currentNode,L,R):
        if currentNode is None:
            return True
        if currentNode.val <= L or currentNode.val>= R:
            return False
        
        leftIsValid = self.validate(currentNode.left,L,currentNode.val)
        return leftIsValid and self.validate(currentNode.right,currentNode.val,R)
                      
                      
        

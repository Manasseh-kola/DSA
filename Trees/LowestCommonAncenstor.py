"""
LeetCode
236. Lowest Common Ancestor of a Binary Tree
Share
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = [None]
        self.traverseTree(root,res,p,q)
        return res[0]
  
    def traverseTree(self,currentNode,res,p,q):
        if currentNode is None:
            return False
        
        left = self.traverseTree(currentNode.left,res,p,q)
        right = self.traverseTree(currentNode.right,res,p,q)
        
        mid = currentNode == p or currentNode == q
        if mid + left + right >=2:
            res[0] = currentNode
          
        return mid or left or right
            

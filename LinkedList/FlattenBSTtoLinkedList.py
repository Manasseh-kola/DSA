"""
LeetCode 114. Flatten Binary Tree to Linked List
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []
        self.preOrder(root,nodes)
        currentNode = root
        
        for i in range(1,len(nodes)):
            currentNode.left = None
            currentNode.right = nodes[i]
            currentNode = currentNode.right
            
        
    def preOrder(self,currentNode,nodes):
        
        if currentNode is not None:
            nodes.append(currentNode)
            self.preOrder(currentNode.left,nodes)
            self.preOrder(currentNode.right,nodes)

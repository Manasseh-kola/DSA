"""
1382. Balance a Binary Search Tree
Medium
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        inOrderArray = []
        self.inOrderTraverse(root,inOrderArray)
        return self.constructMinHeight(inOrderArray,0,len(inOrderArray)-1)
        
    def constructMinHeight(self,array,L,R):
        if L>R:
            return None
        M =(L+R)//2
        bst = TreeNode(array[M])
        bst.left = self.constructMinHeight(array,L,M-1)
        bst.right = self.constructMinHeight(array,M+1,R)
        return bst
    
    def inOrderTraverse(self,tree,array):
        if tree is None:
            return
        self.inOrderTraverse(tree.left,array)
        array.append(tree.val)
        self.inOrderTraverse(tree.right,array)
        return array

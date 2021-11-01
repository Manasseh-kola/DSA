"""
LeetCode
143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        listArray = []
        currentNode = head
        
        while currentNode:
            listArray.append(currentNode)
            currentNode = currentNode.next
        
        currentNode = head
        while currentNode and len(listArray):
            nextNode = currentNode.next
            lastNode = listArray.pop()
            if currentNode == lastNode or lastNode == nextNode:
                return head
            currentNode.next = lastNode
            lastNode.next = nextNode
            if len(listArray):
                listArray[-1].next = None
            currentNode = nextNode
            

"""
25. Reverse Nodes in k-Group
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        sentinel = ListNode(0,head)
        prevNode = sentinel
        currentNode = head
        index = 1
        currentStart = None
        currentEnd = None
        
        while currentNode:
            nextNode = currentNode.next
            if index == 1:
                currentStart = currentNode
            if index == k:
                currentEnd = currentNode
                currentEnd.next = None
                reversedList = self.reverseList(currentStart)
                prevNode.next = reversedList
                currentStart.next = nextNode
                prevNode = currentStart
                index =0
          
            currentNode = nextNode
            index+=1
            
        return sentinel.next
            
        
    def reverseList(self,head):
        prevNode = None
        currentNode = head
        
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        
        return prevNode

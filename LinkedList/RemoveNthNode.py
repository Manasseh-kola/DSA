"""
Leetcode
19. Remove Nth Node From End of List.
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        count = 0
        sentinel = ListNode()
        sentinel.next = head
        currentNode = sentinel
        prevRemoveNode = sentinel
        
        while currentNode is not None:
            if count >= n+1:
                prevRemoveNode = prevRemoveNode.next
            currentNode = currentNode.next
            count +=1
            
        prevRemoveNode.next = prevRemoveNode.next.next
        
        return sentinel.next
        

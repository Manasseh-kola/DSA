"""
61. Rotate List
Given the head of a linked list, rotate the list to the right by k places.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        listArray = []
        currentNode = head
        lenList = 0
        if head is None or head.next is None or k == 0:
            return head
        
        while currentNode is not None:
            lenList +=1
            listArray.append(currentNode)
            currentNode = currentNode.next
        
        newHeadIndex = lenList-(k%lenList)
        if newHeadIndex == 0 or newHeadIndex == lenList:
            return head
        
        prevIndex = newHeadIndex -1
        listArray[prevIndex].next = None
        listArray[-1].next = listArray[0]
        return listArray[newHeadIndex]
        

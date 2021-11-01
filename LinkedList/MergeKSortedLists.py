"""
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        sentinel = ListNode(float("-inf"))
        prevList = sentinel
        for currentList in lists:
            if currentList is None:
                continue
            prevList = self.sortList(prevList,currentList)
            
        return sentinel.next
        
    def sortList(self,l1,l2):
        
        if l1 is None:
            return l2
        if l2 is None:
            return 11
        
        sentinel = ListNode()
        prev = sentinel
        node1,node2 = l1,l2
        
        while node1 is not None and node2 is not None:
            nextPrev = node1 if node1.val <= node2.val else node2
            nextNode = node1 if nextPrev == node2 else node2
            
            if nextPrev == node1:
                node1 = node1.next
            else:
                node2 = node2.next
            
            prev.next = nextPrev
            nextPrev.next = nextNode
            prev = nextPrev
            
        return sentinel.next

"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        carry = 0
        sumList = ListNode()
        node1 = l1
        node2 = l2
        currentSumNode = sumList
        
        while node1 is not None or node2 is not None:
            num1 = node1.val if node1 is not None else 0
            num2 = node2.val if node2 is not None else 0
            
            currentSum = num1+num2+carry
            carry = currentSum//10
            currentValue = currentSum%10
            currentSumNode.val =currentValue
            
            node1 = node1.next if node1 is not None else None
            node2 = node2.next if node2 is not None else None
            
            if node1 or node2:
                currentSumNode.next = ListNode()
                currentSumNode = currentSumNode.next
                
        if carry !=0:
            currentSumNode.next = ListNode(carry)
        
        return sumList
     

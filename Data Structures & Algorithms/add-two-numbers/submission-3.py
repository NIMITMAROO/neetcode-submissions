# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        l3 = dummy 
        curr1 = l1
        curr2 = l2
        carry = 0

        while curr1 != None or curr2 != None:

            if curr1:
                val1 = curr1.val
            else:
                val1 = 0
            
            if curr2:
                val2 = curr2.val
            
            else:
                val2 = 0
            
            sum = val1 + val2 + carry

            l3.next = ListNode(sum % 10)
            l3 = l3.next
            carry = sum // 10

            if curr1:
                curr1 = curr1.next
            
            if curr2:
                curr2 = curr2.next
            
        if carry:
            l3.next = ListNode(carry)
        
        return dummy.next
            



        
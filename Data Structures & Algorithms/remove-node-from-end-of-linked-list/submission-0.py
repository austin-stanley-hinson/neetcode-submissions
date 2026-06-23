# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Edge Case: No node is given 
        if not head:
            return None 

        dummy = ListNode(next=head)
        fast, slow = dummy, dummy 

        for _ in range(n):
            fast = fast.next 
        
        while fast and fast.next:
            fast = fast.next
            slow = slow.next 
        
        slow.next = slow.next.next 

        return dummy.next 

        '''
        dummy -> 5
        s        f

        '''


        

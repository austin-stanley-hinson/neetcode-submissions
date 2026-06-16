# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #  1 -> 3 -> 4 -> 5 
        #  1 -> 2 -> ... 
        #  2 -> 5 -> ....

        # 5431 + 21 = 5452

        #keep adding the values in the nodes and storing sums to create the return LL
        #if any of them runs out of nodes, use 0 

        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        prev = dummy 
        carry_over = False

        while cur1 or cur2:                 

            if cur1 and cur2:
                if carry_over:
                    cur1.val = cur1.val + 1
                    carry_over = False

                node_sum = cur1.val + cur2.val
                if node_sum > 9:
                    node = ListNode(node_sum - 10)
                    carry_over = True
                    prev.next = node
                    prev = node
                    cur1 = cur1.next
                    cur2 = cur2.next
                else:
                    prev.next = ListNode(cur1.val + cur2.val)
                    prev = prev.next 
                    cur1 = cur1.next 
                    cur2 = cur2.next 
            elif cur1:
                if carry_over:
                    cur1.val = 1 + cur1.val
                    carry_over = False

                if cur1.val > 9:
                    carry_over = True
                    prev.next = ListNode(cur1.val - 10)
                    prev = prev.next 
                    cur1 = cur1.next
                else:
                    prev.next = ListNode(cur1.val)
                    prev = prev.next 
                    cur1 = cur1.next

            elif cur2:
                if carry_over:
                    cur2.val = 1 + cur2.val
                    carry_over = False

                if cur2.val > 9:
                    carry_over = True
                    prev.next = ListNode(cur2.val - 10)
                    prev = prev.next 
                    cur2 = cur2.next
                else:
                    prev.next = ListNode(cur2.val)
                    prev = prev.next 
                    cur2 = cur2.next
        if carry_over:
            prev.next = ListNode(1)

        return dummy.next 

        '''

        (dummy) -> 0 -> 0
        #cur1 = 1 
        #cur2 = None
        #carry_over = T

        #while cur1 or cur2:


        '''


            


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        prev = dummy 

        cur1, cur2 = l1, l2
        carry_over = 0 

        while cur1 or cur2 or carry_over:
            
            val1 = cur1.val if cur1 else 0
            val2 = cur2.val if cur2 else 0

            total = val1 + val2 + carry_over

            carry_over = total // 10

            prev.next = ListNode(total % 10)
            prev = prev.next 

            if cur1:
                cur1 = cur1.next
            if cur2:
                cur2 = cur2.next

        return dummy.next 

        '''
         5 -> 4 -> 5         .....545 , sum = 7881
         6 -> 3 -> 3 -> 7 ....7336 

         cur1 = None
         cur2 = None
         carry_over = 0

         dummy = Node(0)
         prev = dummy 

         dummy -> Node(1) -> Node(8) -> Node(8) -> Node(7)
                                                    prev 

         while cur1 or cur2 or carry_over:
            cur1.val = 0
            cur2.val = 7

            total = 7 + 0 + 0 = 7 

            carry_over = 8 % 10 = 0
            temp = _ // 10 = int(0..) = 0 

            prev.next = Node(7)

        is_alive = false;
        cout << is_alive; ...0 

        '''

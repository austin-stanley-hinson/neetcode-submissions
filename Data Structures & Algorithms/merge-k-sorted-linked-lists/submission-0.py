# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]
        
        mid = len(lists)//2

        left_half = self.mergeKLists(lists[:mid])
        right_half = self.mergeKLists(lists[mid:])

        return self.mergeTwoLists(left_half, right_half)

    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        prev = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
                prev = prev.next 
            else:
                prev.next = list2
                list2 = list2.next 
                prev = prev.next 
        
        prev.next = list1 if list1 else list2

        return dummy.next 
            
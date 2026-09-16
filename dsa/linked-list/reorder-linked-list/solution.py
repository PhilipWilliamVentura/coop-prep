# Pattern: Split, reverse, and merge
# Time: O(n) | Space: O(1)
# Tripped up on: Find the half to split using fast and slow pointers. then reverse the second half

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        start1, start2 = head, prev
        while start1 and start2:
            temp = start1.next
            start1.next = start2
            start1 = temp
            temp = start2.next
            start2.next = start1
            start2 = temp
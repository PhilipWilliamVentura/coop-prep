# Pattern: Merge two linked lists at the time and keep merging
# Time: O(n * log(k)) | Space: O(k)
# Tripped up on: Go though lists by steps of 2 and merge two linked lists at the time.
#                Append the merged lists into an array and at the end of the loop redefine lists as the array
#                Repeat until len(lists) == 0

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(self.mergelists(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergelists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next

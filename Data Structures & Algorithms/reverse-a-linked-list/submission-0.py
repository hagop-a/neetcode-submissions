# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nd = head
        prev = None

        while nd:
            temp = nd.next
            nd.next = prev
            prev = nd
            nd = temp
        return prev

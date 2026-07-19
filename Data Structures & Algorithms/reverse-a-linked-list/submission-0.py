# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # Save next node
            curr.next = prev     # Reverse link
            prev = curr          # Move prev
            curr = nxt           # Move curr

        return prev
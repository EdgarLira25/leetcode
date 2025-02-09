# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        items = set()
        while head:
            if head.next in items:
                return True
            items.add(head.next)
            head = head.next

        return False

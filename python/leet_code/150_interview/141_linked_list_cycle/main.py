from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode], track: set = set()) -> bool:
        if not head:
            return False

        if head in track:
            return True

        track.add(head)
        return self.hasCycle(head.next, track)

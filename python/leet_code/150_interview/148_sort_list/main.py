from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        min_val = self.find_min(head)
        if min_val == head:
            head = head.next

        new_head = min_val
        current_min = min_val
        next_min = min_val
        while current_min:
            next_min = self.find_min(head)

            if next_min and next_min == head:
                head = head.next

            current_min.next = next_min
            current_min = next_min

        return new_head

    def find_min(slef, head: Optional[ListNode]) -> ListNode:
        min_val = head
        current = head
        before = None
        before_min = head
        while current:
            if current.val <= min_val.val:
                min_val = current
                before_min = before
            before = current
            current = current.next

        if min_val != head:
            before_min.next = min_val.next

        return min_val


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


def array_to_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


if __name__ == "__main__":
    arr = []
    linked_list = array_to_linked_list(arr)
    print(linked_list)
    head = Solution().sortList(linked_list)
    print_linked_list(head)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = self.linked_list_to_array(head)
        arr.sort()
        return self.array_to_linked_list(arr)

    def linked_list_to_array(self, head: Optional[ListNode]) -> list:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        return arr

    def array_to_linked_list(self, arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        current = head

        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next

        return head


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    arr = [4, 2, 1, 3]
    linked_list = Solution().array_to_linked_list(arr)
    print(linked_list)
    head = Solution().sortList(linked_list)
    print_linked_list(head)

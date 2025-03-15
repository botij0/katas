from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last = None
        nums = set()

        current = head
        while current:
            if current.val not in nums:
                nums.add(current.val)
                last = current
                current = current.next

            else:
                aux = current.next
                last.next = aux
                current = None

                current = aux

        return head


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
    head = [1, 1, 1]
    head = array_to_linked_list(head)
    print_linked_list(head)
    # print(Solution().deleteDuplicates(head))
    print_linked_list(Solution().deleteDuplicates(head))

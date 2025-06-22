class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        nxt = slow.next
        slow.next = None
        slow, prev = nxt, None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        left, right = head, prev
        while right:
            left_nxt, right_nxt = left.next, right.next
            left.next = right
            right.next = left_nxt
            left, right = left_nxt, right_nxt
        return head
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Edge cases
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find length and last node
        length = 1
        tail = head

        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Reduce k
        k = k % length

        if k == 0:
            return head

        # Step 3: Make circular linked list
        tail.next = head

        # Step 4: Find new tail
        steps = length - k - 1
        new_tail = head

        for _ in range(steps):
            new_tail = new_tail.next

        # Step 5: Break the circle
        new_head = new_tail.next
        new_tail.next = None

        return new_head
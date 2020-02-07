def hasCycle(head):
    if head is None or head.next is None:
        return False
    fast, slow = head, head.next
    while fast != slow:
        # fast都走到空了还没相遇，那凉了
        if fast.next is None or fast is None:
            return False

        fast = fast.next.next
        slow = slow.next
    # 能走出while循环就是快慢相遇
    return True
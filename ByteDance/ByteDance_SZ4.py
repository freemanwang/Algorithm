'''
单链表是否有环存在
'''

# 这题在 leetcode/chain 中已经用快慢指针做了，这里就换种办法

def hasCycle(head):
    if not head or head.next == None:
        return False

    nodeSet = set()
    cur = head
    while cur:
        if cur.next in nodeSet:
            return True
        else:
            nodeSet.add(cur)
        cur = cur.next
    return False


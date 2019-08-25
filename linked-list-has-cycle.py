class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    nodesSeen = []
    while head is not None:
        if head in nodesSeen:
            return True
        else:
            nodesSeen.append(head)
        head = head.next
    return False


def hasCycleFaster(head):

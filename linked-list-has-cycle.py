def hasCycle(self, head):
    nodesSeen = []
    while head is not None:
        if head in nodesSeen:
            return True
        else:
            nodesSeen.append(head)
        head = head.next
    return False

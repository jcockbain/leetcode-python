class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(self, root):
    return isMirror(root, root)


def isMirror(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return t1.val == t2.val and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)

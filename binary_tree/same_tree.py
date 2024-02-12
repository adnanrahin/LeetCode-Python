class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        if q is None and p is None:
            return True
        elif q is None or p is None:
            return False
        if q.val != p.val:
            return False
        elif q is not None and p is not None :
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

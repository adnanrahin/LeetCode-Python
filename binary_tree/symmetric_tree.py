class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.check_symmetry(root.left, root.right)

    def check_symmetry(self, root_left, root_right):
        if root_left is None and root_right is None:
            return True
        elif root_left is None or root_right is None:
            return False
        elif root_left.val != root_right.val:
            return False
        elif root_left is not None and root_right is not None:
            return self.check_symmetry(root_left.left, root_right.right) and self.check_symmetry(root_left.right,
                                                                                             root_right.left)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        return self.root_to_leaf_numer_sum(root, 0)

    def root_to_leaf_numer_sum(self, root, sum):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return root.val + (sum * 10)
        left = self.root_to_leaf_numer_sum(root.left, root.val + (sum * 10))
        right = self.root_to_leaf_numer_sum(root.right, root.val + (sum * 10))
        return left + right

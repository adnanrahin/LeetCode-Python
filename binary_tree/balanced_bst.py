class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        if root is None:
            return True
        if abs(self.tree_height(root.left) - self.tree_height(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def tree_height(self, root):
        if root is None:
            return 0
        return max(self.tree_height(root.left), self.tree_height(root.right)) + 1

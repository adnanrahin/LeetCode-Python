class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result = self.travers(root, [])
        return result

    def travers(self, root, result):
        if root is None:
            return result
        result = self.travers(root.left, result)
        result.append(root.val)
        result = self.travers(root.right, result)

        return result

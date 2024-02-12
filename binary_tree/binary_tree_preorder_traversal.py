class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        return self.traverse(root, [])

    def traverse(self, root, result):
        if root is None:
            return result
        result.append(root.val)
        result = self.traverse(root.left, result)
        result = self.traverse(root.right, result)

        return result


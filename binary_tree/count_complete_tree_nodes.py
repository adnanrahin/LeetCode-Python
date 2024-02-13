class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def countNodes(self, root):
        counter = [0] * 2
        return self.count_nodes_in_tree(root, counter)

    def count_nodes_in_tree(self, root, counter):
        if root is None:
            return 0
        self.count_nodes_in_tree(root.left, counter)
        counter[0] += 1
        self.count_nodes_in_tree(root.right, counter)
        return counter[0]

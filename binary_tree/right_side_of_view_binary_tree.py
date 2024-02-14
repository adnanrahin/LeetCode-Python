class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        level_order_map = {}
        self.level_order_tree_traversal(root, 0, level_order_map)
        result = []
        for key, value in level_order_map.items():
            result.append(value[-1])

        return result
    def level_order_tree_traversal(self, root, level, level_order_map):
        if root is None:
            return
        level_order_map.setdefault(level, []).append(root.val)
        self.level_order_tree_traversal(root.left, level + 1, level_order_map)
        self.level_order_tree_traversal(root.right, level + 1, level_order_map)
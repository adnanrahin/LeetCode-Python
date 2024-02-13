class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        if root is None:
            return root
        level_order_map = {}
        self.level_order_traversal(root, 0, level_order_map)
        result = []
        for key, value in level_order_map.items():
            result.append(value)
        return result

    def level_order_traversal(self, root, level, level_order_map):
        if root is None:
            return None
        if level % 2 == 0:
            level_order_map.setdefault(level, []).append(root.val)
        else:
            level_order_map.setdefault(level, []).insert(0, root.val)
        self.level_order_traversal(root.left, level + 1, level_order_map)
        self.level_order_traversal(root.right, level + 1, level_order_map)

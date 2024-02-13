class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return None
        level_order_map = {}
        self.level_order(root, 0, level_order_map)
        result = []
        for key, value in level_order_map.items():
            avg = sum(value) / len(value)
            result.append(avg)
        return result
    def level_order(self, root, level, level_order_map):
        if root is None:
            return
        level_order_map.setdefault(level, []).append(root.val)
        self.level_order(root.left, level + 1, level_order_map)
        self.level_order(root.right, level + 1, level_order_map)
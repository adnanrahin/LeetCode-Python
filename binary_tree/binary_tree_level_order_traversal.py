class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return None
        level_order_map = {}
        self.level_order_dfs(root, 0, level_order_map)
        result = []
        for key, value in level_order_map.items():
            result.append(level_order_map.get(key))
        return result

    def level_order_dfs(self, root, level, level_order_map):
        if root is None:
            return
        if level not in level_order_map:
            level_order_map[level] = []
        level_order_map[level].append(root.val)
        self.level_order_dfs(root.left, level + 1, level_order_map)
        self.level_order_dfs(root.right, level + 1, level_order_map)

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return None
        level_order_map = {}
        self.level_order_dfs(root, 0, level_order_map)
        result = []
        for key, value in level_order_map.items():
            result.append(level_order_map.get(key))
        return result

    def level_order_dfs(self, root, level, level_order_map):
        if root is None:
            return
        level_order_map.setdefault(level, []).append(root.val)
        self.level_order_dfs(root.left, level + 1, level_order_map)
        self.level_order_dfs(root.right, level + 1, level_order_map)
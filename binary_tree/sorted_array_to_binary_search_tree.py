class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        return self.balance_bst(nums, 0, len(nums) - 1)

    def balance_bst(self, nums, low, high):
        if low > high: return None
        mid = low + (high - low) // 2
        root = TreeNode(nums[mid])
        root.left = self.balance_bst(nums, low, mid - 1)
        root.right = self.balance_bst(nums, mid + 1, high)
        return root

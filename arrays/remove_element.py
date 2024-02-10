class Solution(object):
    def removeElement(self, nums, val):
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
                right -= 1
            else:
                left += 1
        return left


print(Solution().removeElement([3, 23, 2, 3, 2, 3, 2, 3, 2, 3], 3))

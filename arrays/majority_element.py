class Solution(object):
    def majorityElement(self, nums):
        cur = 0
        count = 0
        for i in range(0, len(nums)):
            if count == 0:
                cur = nums[i]
            if nums[i] == cur:
                count += 1
            else:
                count -= 1

        return cur


print(Solution().majorityElement([3, 3, 4]))

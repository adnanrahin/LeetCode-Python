class Solution(object):
    def twoSum(self, nums, target):
        duplicates = {}
        for i in range(len(nums)):
            sum = target - nums[i]
            if sum in duplicates:
                return {i, duplicates[sum]}
            else:
                duplicates[nums[i]] = i

        return {0, 0}


nums = [2, 7, 11, 15]
print(Solution().twoSum(nums, 9))
print(Solution().twoSum([3,3], 6))
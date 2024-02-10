class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        start = len(nums) - k
        res = []
        for i in range(start, len(nums)):
            res.append(nums[i])

        for i in range(start):
            res.append(nums[i])

        for i in range(len(nums)):
            nums[i] = res[i]

        return nums


print(Solution().rotate([1, 2, 3, 4, 5], 3))
print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))

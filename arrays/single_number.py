from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


print(Solution().singleNumber([1, 2, 2]))
print(Solution().singleNumber([2, 2, 1]))

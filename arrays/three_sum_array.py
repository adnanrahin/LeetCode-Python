class Solution(object):
    def threeSum(self, nums):
        sorted_num = sorted(nums)
        result = []
        for i in range(len(sorted_num) - 2):
            left = i + 1
            right = len(sorted_num) - 1
            if i > 0 and sorted_num[i] == sorted_num[i - 1]:
                continue
            while left < right:
                if right < len(sorted_num) - 1 and sorted_num[right + 1] == sorted_num[right]:
                    right -= 1
                    continue
                sum = sorted_num[i] + sorted_num[left] + sorted_num[right]
                if sum == 0:
                    res = [sorted_num[i], sorted_num[left], sorted_num[right]]
                    right -= 1
                    left += 1
                    result.append(res)
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return result


nums = [-2,0,0,2,2]
print(Solution().threeSum(nums))

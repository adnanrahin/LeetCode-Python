class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}
        for i in range(len(nums)):
            if nums[i] not in index_map:
                index_map[nums[i]] = i
            elif nums[i] in index_map:
                if abs(index_map[nums[i]] - i) <= k:
                    return True
                else:
                    index_map[nums[i]] = i

        return False

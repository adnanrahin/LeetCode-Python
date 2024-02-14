import heapq
from typing import List


class Solution(object):
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            if len(pq) < k:
                heapq.heappush(pq, num)
            elif len(pq) == k:
                if num > pq[0]:
                    heapq.heappop(pq)
                    heapq.heappush(pq, num)
        return pq[0]

arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
nums = [3,2,1,5,6,4]
print(Solution().findKthLargest(arr, 4))
print(Solution().findKthLargest(nums, 2))

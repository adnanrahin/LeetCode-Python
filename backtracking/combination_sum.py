from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        global_result = []
        self.back_tracking_combination_sum(candidates, target, 0, result, global_result)
        return global_result

    def back_tracking_combination_sum(self, candidates: List[int], target: int, start: int, result: List[int],
                                      global_result: List[List[int]]):
        if target < 0:
            return

        if target == 0:
            global_result.append(result[:])
            return

        for i in range(start, len(candidates)):
            result.append(candidates[i])
            self.back_tracking_combination_sum(candidates, target - candidates[i], i, result, global_result)
            result.pop()


print(Solution().combinationSum([2, 3, 6, 7], 7))

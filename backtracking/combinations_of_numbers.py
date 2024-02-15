from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        solution = []
        self.back_tracking_number_combinations(n, k, 1, result, solution)
        return solution

    def back_tracking_number_combinations(self, n, k, start, res, solution):
        if len(res) == k:
            solution.append(res[:])
            return
        for i in range(start, n + 1):
            res.append(i)
            self.back_tracking_number_combinations(n, k, i + 1, res, solution)
            res.pop()

print(Solution().combine(50, 20))
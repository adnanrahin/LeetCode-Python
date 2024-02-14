from typing import List


class Solution:
    keypad = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        result = []
        self.back_track(digits, 0, "", result)
        return result

    def back_track(self, digit: str, count: int, key: str, result: List[str]):
        if len(digit) == len(key):
            result.append(key)
            return
        keys = self.keypad[digit[count]]
        for c in keys:
            self.back_track(digit, count + 1, key + c, result)
        return
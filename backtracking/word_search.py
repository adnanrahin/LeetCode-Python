from typing import List


class Solution:
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def exist(self, board: List[List[str]], word: str) -> bool:

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.word_search_back_track(board, word, 0, row, col):
                        return True

        return False

    def word_search_back_track(self, grid: List[List[str]], word: str, count, row, col) -> bool:

        if len(word) == count:
            return True

        if not self.isValid(grid, row, col):
            return False
        if grid[row][col] == '*' or grid[row][col] != word[count]:
            return False

        letter = grid[row][col]
        grid[row][col] = '*'

        for dirs in self.directions:
            r = row + dirs[0]
            c = col + dirs[1]
            if self.word_search_back_track(grid, word, count + 1, r, c):
                return True
        grid[row][col] = letter

        return False

    def isValid(self, board: List[List[str]], row, col):
        return 0 <= row < len(board) and 0 <= col < len(board[0])


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

print(Solution().exist(board, word))

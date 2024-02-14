class Solution(object):
    directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    def numIslands(self, grid):
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    self.depth_first_search(grid, row, col)
                    count += 1

        return count
    def depth_first_search(self, grid, row, col):
        if not self.is_valid(grid, row, col):
            return
        if grid[row][col] == "0":
            return
        grid[row][col] = "0"
        for dir in self.directions:
            r = row + dir[0]
            c = col + dir[1]
            self.depth_first_search(grid, r, c)

    def is_valid(self, grid, row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])


grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

print(Solution().numIslands(grid))
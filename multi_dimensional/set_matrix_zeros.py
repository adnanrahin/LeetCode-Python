class Solution(object):
    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        pos = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    pos.append([i, j])

        for i in range(len(pos)):
            r = pos[i][0]
            c = pos[i][1]
            for j in range(col):
                matrix[r][j] = 0

            for j in range(row):
                matrix[j][c] = 0
        return matrix

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

print(Solution().setZeroes(matrix))
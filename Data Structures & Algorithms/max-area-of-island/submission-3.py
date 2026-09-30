class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = [[False] * cols for _ in range(rows)]

        def recur(i, j):
            if not (0 <= i < rows) or not (0 <= j < cols) or grid[i][j] == 0 or visited[i][j]:
                return 0

            visited[i][j] = True

            s = 1

            for k, l in dirs:
                s += recur(i+k, j+l)
            return s

        res = 0

        for i in range(rows):
            for j in range(cols):
                res = max(res, recur(i, j))

        return res
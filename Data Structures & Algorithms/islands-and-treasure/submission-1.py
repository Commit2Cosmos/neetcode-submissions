from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def bfs(i, j):
            if not (0 <= i < rows) or not (0 <= j < cols) or grid[i][j] == -1:
                return float('inf')
            if grid[i][j] == land:
                return 0
            
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i,j))

        while queue:
            i, j = queue.popleft()

            for (k, l) in directions:
                ni, nj = i+k, j+l

                if (0 <= ni < rows) and (0 <= nj < cols) and grid[ni][nj] == land:
                    grid[ni][nj] = 1 + grid[i][j]
                    queue.append((ni, nj))
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        island_count = 0
        visited = [[False] * cols for _ in range(rows)]

        def dfs(i, j):
            if not (0 <= i < rows and 0 <= j < cols) or grid[i][j] == "0" or visited[i][j] is True:
                return

            visited[i][j] = True

            for (k, l) in [(0,1), (0,-1), (1,0), (-1,0)]:
                dfs(i+k, j+l)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0" or visited[i][j] is True:
                    continue
                
                island_count += 1

                dfs(i, j)

        return island_count
                

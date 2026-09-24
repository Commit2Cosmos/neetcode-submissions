class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        pacific_set = set()
        atlantic_set = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(i, j, visited):

            visited.add((i, j))

            for (k,l) in dirs:
                ni = i+k
                nj = j+l
                if (0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited and heights[ni][nj] >= heights[i][j]):
                    dfs(ni, nj, visited)


        for j in range(cols):
            dfs(0, j, pacific_set)
            dfs(rows-1, j, atlantic_set)

        for i in range(rows):
            dfs(i, 0, pacific_set)
            dfs(i, cols-1, atlantic_set)

        return list(pacific_set & atlantic_set)

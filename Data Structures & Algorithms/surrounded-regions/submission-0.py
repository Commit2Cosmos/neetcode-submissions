class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = [[False]*len(board[0]) for _ in range(len(board))]

        def dfs(i, j):
            if not i in range(len(board)) or not j in range(len(board[0])) or board[i][j] == "X" or visited[i][j]:
                return

            visited[i][j] = True

            for k,l in dirs:
                dfs(i+k, j+l)

        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board)-1, j)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0])-1)

        for i in range(1, len(board)-1):
            for j in range(1, len(board[0])-1):
                if not visited[i][j]:
                    board[i][j] = "X"

                
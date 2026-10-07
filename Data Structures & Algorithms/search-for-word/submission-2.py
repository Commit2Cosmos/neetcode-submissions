class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def recur(i,j,k,visited):
            if k == len(word):
                return True

            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])):
                return False

            if visited[i][j]:
                return False
            
            visited[i][j] = True

            res = False
            if board[i][j] == word[k]:
                for p,q in dirs:
                    res = res or recur(i+p, j+q, k+1, visited)

            visited[i][j] = False
            return res

        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = [[False]*len(board[0]) for _ in range(len(board))]
                res = res or recur(i,j,0,visited)


        return res
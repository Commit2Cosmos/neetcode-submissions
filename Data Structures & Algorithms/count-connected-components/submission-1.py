class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        edge_map = {}

        for x, y in edges:
            if x in edge_map:
                edge_map[x].append(y)
            else:
                edge_map[x] = [y]

            if y in edge_map:
                edge_map[y].append(x)
            else:
                edge_map[y] = [x]

        visited = [False]*n
        count = 0

        for i in range(n):
            if visited[i]:
                continue

            if i not in edge_map:
                count += 1
                visited[i] = True
                continue
            
            stack = edge_map[i].copy()

            while len(stack) > 0:
                node = stack.pop()
                
                if visited[node]:
                    continue

                visited[node] = True
                
                for x in edge_map[node]:
                    stack.append(x)

                
            count += 1
            

        return count